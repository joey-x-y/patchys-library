################################################################################
## STATEFUL SPRITE HELPERS
##
## Examples:
##
##     $ flan.show()
##     $ flan.show(expression="frown")
##     $ flan.move(left)
##     $ flan.hide()
##
##     $ pat.show(expression="angry", magic=True)
##     $ remi.show(dirty=True)
##
################################################################################


init python:

    # Current schemas keyed by tag. Init-time sprite construction fills this;
    # old saves keep stale self.defaults, so normalize reads from here instead.
    STATEFUL_SPRITE_SCHEMAS = {}
    DEFAULT_SPRITE_ZORDER = 5

    class StatefulSprite:
        """
        Controls a set of complete, flattened character sprites as though their
        properties were independently selectable.

        The lookup table maps logical state combinations to Ren'Py image names.
        """

        def __init__(
            self,
            tag,
            state_order,
            defaults,
            lookup=None,
            compose=None,
            layer="master",
            zorder=DEFAULT_SPRITE_ZORDER,
        ):
            if lookup is None and compose is None:
                raise Exception(
                    "StatefulSprite {!r} requires a lookup table or compose function.".format(tag)
                )

            self.tag = tag
            self.state_order = tuple(state_order)
            self.defaults = defaults.copy()
            self.state = defaults.copy()
            self.lookup = lookup or {}
            self.compose = compose
            self.layer = layer
            self.flipped = False
            self.zorder = zorder

            # Remember the last position used by move() or show(position=...).
            self.position = None

            STATEFUL_SPRITE_SCHEMAS[tag] = {
                "defaults": defaults.copy(),
                "state_order": tuple(state_order),
                "compose": compose,
            }


        ########################################################################
        ## Internal methods
        ########################################################################

        def _state_key(self, state=None):
            """
            Converts a state dictionary into the tuple used by the lookup table.
            """

            if state is None:
                state = self.state

            return tuple(state[name] for name in self.state_order)


        def _ensure_runtime_attrs(self):
            """
            Fill instance fields added in later builds (old saves omit them).
            """

            if not hasattr(self, "zorder"):
                self.zorder = DEFAULT_SPRITE_ZORDER

            if not hasattr(self, "flipped"):
                self.flipped = False

            if not hasattr(self, "position"):
                self.position = None


        def _sync_schema(self):
            """
            Refresh defaults/state_order/compose from the current game definition.

            Saved sprites pickle their own defaults, which go stale when the
            schema changes (e.g. hunt -> glove).
            """

            self._ensure_runtime_attrs()

            schema = STATEFUL_SPRITE_SCHEMAS.get(self.tag)

            if schema is None:
                return

            self.defaults = schema["defaults"].copy()
            self.state_order = schema["state_order"]

            if schema.get("compose") is not None:
                self.compose = schema["compose"]


        def _normalize_state(self, state, persist=False):
            """
            Rebuild state from current defaults when it has missing or obsolete
            keys (common with older saves). Keeps any values that are still valid.
            """

            self._sync_schema()

            expected_keys = set(self.defaults)
            state_keys = set(state)

            if state_keys == expected_keys:
                return state

            rebuilt = self.defaults.copy()

            for key in expected_keys:
                if key in state:
                    rebuilt[key] = state[key]

            if persist:
                self.state = rebuilt

            return rebuilt


        def _image_name(self, state=None):
            """
            Returns the Ren'Py image name for a given state.

            Uses compose() when provided (e.g. layeredimages), otherwise lookup.
            """

            persist = state is None

            if state is None:
                state = self.state

            state = self._normalize_state(state, persist=persist)

            if self.compose is not None:
                try:
                    return self.compose(state)
                except KeyError:
                    # Stale schema or corrupt state: force rebuild from current defaults.
                    self._sync_schema()
                    state = self.defaults.copy()
                    self.state = state
                    return self.compose(state)

            key = self._state_key(state)

            if key not in self.lookup:
                state_description = ", ".join(
                    "{}={!r}".format(name, state[name])
                    for name in self.state_order
                )

                raise Exception(
                    "No sprite exists for {} with state: {}".format(
                        self.tag,
                        state_description,
                    )
                )

            return self.lookup[key]


        def _apply_transition(self, transition):
            """
            Runs a Ren'Py transition when one was supplied.
            """

            if transition is not None:
                renpy.with_statement(transition)


        ########################################################################
        ## Main public methods
        ########################################################################

        def show(
            self,
            at=None,
            transition=None,
            zorder=None,
            behind=None,
            reset=False,
            flip=False,
            **changes
        ):
            """
            Shows the character or changes their current appearance.

            Any omitted properties retain their existing values.

            Examples:

                $ flan.show()
                $ flan.show(expression="frown")
                $ flan.show(wings="mid", accessories=False)
                $ flan.show(at=left)
                $ flan.show(expression="frown", transition=dissolve)
                $ flan.show(reset=True)
            """

            self._sync_schema()

            if reset:
                proposed_state = self.defaults.copy()
            else:
                # Rebuild from defaults if this save has obsolete/missing keys,
                # then keep any values that are still valid.
                proposed_state = self._normalize_state(self.state, persist=True).copy()

            # Reject misspelled or unsupported property names.
            for name in changes:
                if name not in self.defaults:
                    raise Exception(
                        "{} has no sprite property named {!r}. "
                        "Valid properties are: {}".format(
                            self.tag,
                            name,
                            ", ".join(self.state_order),
                        )
                    )

            proposed_state.update(changes)

            # Validate before changing the stored state.
            image_name = self._image_name(proposed_state)

            was_showing = renpy.showing(
                self.tag,
                layer=self.layer,
            )

            if zorder is not None:
                self.zorder = zorder

            show_arguments = {
                "layer": self.layer,
                "zorder": self.zorder,
            }

            if behind is not None:
                show_arguments["behind"] = behind

            if flip:
                self.flip()

            if at is not None:

                # Remember it.
                self.position = at

                if isinstance(at, (list, tuple)):
                    show_arguments["at_list"] = list(at)
                else:
                    show_arguments["at_list"] = [at]

                show_arguments["at_list"].append(sprite_facing(self.flipped))

            elif not was_showing and self.position is not None:

                if isinstance(self.position, (list, tuple)):
                    show_arguments["at_list"] = list(self.position)
                else:
                    show_arguments["at_list"] = [self.position]

                show_arguments["at_list"].append(sprite_facing(self.flipped))

            renpy.show(
                image_name,
                **show_arguments
            )

            self._sync_companions(show_arguments)

            self.state = proposed_state
            self._apply_transition(transition)

            return image_name


        def move(self, at, transition=None, zorder=None):
            """
            Moves the character while preserving their current appearance.

            Examples:

                $ flan.move(left)
                $ flan.move(center, transition=move)
            """

            self._sync_schema()

            self.position = at

            if zorder is not None:
                self.zorder = zorder

            if renpy.showing(self.tag, layer=self.layer):

                if isinstance(at, (list, tuple)):
                    at_list = list(at)
                else:
                    at_list = [at]

                at_list.append(sprite_facing(self.flipped))

                show_arguments = {
                    "layer": self.layer,
                    "at_list": at_list,
                    "zorder": self.zorder,
                }

                renpy.show(
                    self._image_name(),
                    **show_arguments
                )

                self._sync_companions(show_arguments)

                self._apply_transition(transition)

        def effect(self, at, transition=None):
            """
            Applies an effect to the character.
            """

            self._sync_schema()

            if self.position is None:
                at_list = []
            elif isinstance(self.position, (list, tuple)):
                at_list = list(self.position)
            else:
                at_list = [self.position]

            if isinstance(at, (list, tuple)):
                at_list.extend(at)
            else:
                at_list.append(at)

            at_list.append(sprite_facing(self.flipped))

            show_arguments = {
                "layer": self.layer,
                "at_list": at_list,
                "zorder": self.zorder,
            }

            renpy.show(
                self._image_name(),
                **show_arguments
            )

            self._sync_companions(show_arguments)

            self._apply_transition(transition)

        def face(self, flipped=True, transition=None):
            self.flipped = flipped

            if renpy.showing(self.tag, layer=self.layer):
                self.show(at=self.position, transition=transition)


        def hide(self, transition=None):
            """
            Hides the character.

            Their appearance state and last position are remembered.

            Examples:

                $ flan.hide()
                $ flan.hide(transition=dissolve)
            """

            renpy.hide(
                self.tag,
                layer=self.layer,
            )

            self._hide_companions()

            self._apply_transition(transition)


        def _sync_companions(self, show_arguments):
            """
            Hook for companion images that should track this sprite.
            """

            pass


        def _hide_companions(self):
            """
            Hook for hiding companion images.
            """

            pass

        def flip(self, transition=None):
            self.face(flipped=not self.flipped, transition=transition)


        def reset(self, at=None, transition=None):
            """
            Restores and shows the character's default appearance.

            The last at is retained unless a new one is supplied.

            Examples:

                $ flan.reset()
                $ flan.reset(at=left)
            """

            return self.show(
                reset=True,
                at=at,
                transition=transition,
            )


        def reset_state(self):
            """
            Restores the default state without showing the character.
            """

            self.state = self.defaults.copy()


        def forget_position(self):
            """
            Clears the remembered screen position.
            """

            self.position = None


        def current_image(self):
            """
            Returns the current Ren'Py image name, useful while debugging.

            Example:

                $ renpy.notify(flan.current_image())
            """

            return self._image_name()


        ########################################################################
        ## Generic state-changing shortcuts
        ########################################################################

        def expression(self, value, transition=None):
            return self.show(
                expression=value,
                transition=transition,
            )


        def dirty(self, value=True, transition=None):
            return self.show(
                dirty=value,
                transition=transition,
            )


        def glove(self, value="On", transition=None):
            return self.show(
                glove=value,
                transition=transition,
            )


        def wings(self, value, transition=None):
            return self.show(
                wings=value,
                transition=transition,
            )


        def accessories(self, value=True, transition=None):
            return self.show(
                accessories=value,
                transition=transition,
            )


        def magic(self, value=True, transition=None):
            return self.show(
                magic=value,
                transition=transition,
            )


        def hat(self, value=True, transition=None):
            return self.show(
                hat=value,
                transition=transition,
            )

        def blush(self, value=True, transition=None):
            return self.show(
                blush=value,
                transition=transition,
            )


################################################################################
## FLAN
################################################################################

init python:

    FLAN_EXPRESSIONS = (
        "neutral",
        "frown",
        "angry",
        "crying",
        "holding_tear",
        "serious",
        "smile",
        "surprised",
    )

    # Script values ("default") map onto layeredimage wing attributes.
    FLAN_WINGS = {
        "default": "begin",
        "mid": "mid",
        "gone": "gone",
        "crystal": "crystal",
    }

    def flan_compose(state):
        """
        Builds a layeredimage attribute name for Flan.

        Wings and face map directly. Base is clean or noacc.
        Dirty and blush are optional overlay attributes.
        """

        expression = state["expression"]

        if expression not in FLAN_EXPRESSIONS:
            raise Exception(
                "Flan has no expression {!r}. Valid expressions are: {}".format(
                    expression,
                    ", ".join(FLAN_EXPRESSIONS),
                )
            )

        wings = state["wings"]

        if wings not in FLAN_WINGS:
            raise Exception(
                "Flan has no wing state {!r}. Valid wings are: {}".format(
                    wings,
                    ", ".join(sorted(FLAN_WINGS)),
                )
            )

        parts = [
            "f",
            FLAN_WINGS[wings],
            expression,
        ]

        if state["hair"] == "long":
            parts.append("long")
        else:
            parts.append("short")

        if state["hat"]:
            parts.append("ribbon")
        else:
            parts.append("nohat")

        if state["tired"]:
            parts.append("tired")
        else:
            parts.append("awake")

        if state["blush"]:
            parts.append("blushing")
        else:
            parts.append("noeffect")

        if state["dirty"]:
            parts.append("dirty")
        else:
            parts.append("none")

        return " ".join(parts)


    FLAN_STATE_ORDER = (
        "expression",
        "hair",
        "hat",
        "dirty",
        "wings",
        "tired",
        "blush",
    )

    FLAN_DEFAULTS = {
        "expression": "neutral",
        "hair": "long",
        "hat": True,
        "dirty": False,
        "wings": "default",
        "tired": False,
        "blush": False,
    }

    STATEFUL_SPRITE_SCHEMAS["f"] = {
        "defaults": FLAN_DEFAULTS.copy(),
        "state_order": FLAN_STATE_ORDER,
        "compose": flan_compose,
    }


default flan = StatefulSprite(
    tag="f",
    state_order=FLAN_STATE_ORDER,
    defaults=FLAN_DEFAULTS,
    compose=flan_compose,
)


################################################################################
## PAT
################################################################################

init python:

    PAT_EXPRESSIONS = (
        "neutral",
        "angry",
        "serious",
        "smile",
        "surprised",
        "think",
    )

    def pat_compose(state):
        """
        Builds a layeredimage attribute name for Patchy.

        Base from hat + magic: base, magic, nohat, magicnohat.
        """

        expression = state["expression"]

        if expression not in PAT_EXPRESSIONS:
            raise Exception(
                "Pat has no expression {!r}. Valid expressions are: {}".format(
                    expression,
                    ", ".join(PAT_EXPRESSIONS),
                )
            )

        parts = [
            "p",
            expression,
        ]

        if state["hat"]:
            parts.append("hat")
        else:
            parts.append("nohat")

        if state["magic"]:
            parts.append("magic")
        else:
            parts.append("base")

        if state["blush"]:
            parts.append("blushing")
        else:
            parts.append("noeffect")

        return " ".join(parts)


    PAT_STATE_ORDER = (
        "expression",
        "hat",
        "magic",
        "blush",
    )

    PAT_DEFAULTS = {
        "expression": "neutral",
        "hat": True,
        "magic": False,
        "blush": False,
    }

    STATEFUL_SPRITE_SCHEMAS["p"] = {
        "defaults": PAT_DEFAULTS.copy(),
        "state_order": PAT_STATE_ORDER,
        "compose": pat_compose,
    }


default pat = StatefulSprite(
    tag="p",
    state_order=PAT_STATE_ORDER,
    defaults=PAT_DEFAULTS,
    compose=pat_compose,
)


################################################################################
## REMI
################################################################################

init python:

    REMI_EXPRESSIONS = (
        "neutral",
        "angry",
        "crying",
        "crying2",
        "embarrassed",
        "serious",
        "smile",
        "surprised",
    )

    REMI_WING_LAYER = "master"
    REMI_WING_ZORDER = 1
    REMI_WING_IMAGE = "r_wings"

    def remi_compose(state):
        """
        Builds a layeredimage attribute name for Remi.

        Base is hunt, noacc, or clean.
        Dirty is an optional overlay attribute.
        """

        expression = state["expression"]

        if expression not in REMI_EXPRESSIONS:
            raise Exception(
                "Remi has no expression {!r}. Valid expressions are: {}".format(
                    expression,
                    ", ".join(REMI_EXPRESSIONS),
                )
            )

        parts = [
            "r",
            expression,
        ]

        if not state["hat"]:
            parts.append("nohat")
        else:
            parts.append("hat")

        if state["glove"] == "Off":
            parts.append("noglove")
        elif state["glove"] == "Blood":
            parts.append("bloody")
        else:
            parts.append("glove")    

        if not state["tired"]:
            parts.append("awake")
        else:
            parts.append("tired")

        if state["blush"]:
            parts.append("blushing")
        else:
            parts.append("noeffect")

        if state["dirty"]:
            parts.append("dirty")
        else:
            parts.append("none")

        return " ".join(parts)


    REMI_STATE_ORDER = (
        "expression",
        "hat",
        "glove",
        "tired",
        "dirty",
        "blush",
    )

    REMI_DEFAULTS = {
        "expression": "neutral",
        "hat": True,
        "glove": "On",
        "tired": False,
        "dirty": False,
        "blush": False,
    }

    STATEFUL_SPRITE_SCHEMAS["r"] = {
        "defaults": REMI_DEFAULTS.copy(),
        "state_order": REMI_STATE_ORDER,
        "compose": remi_compose,
        "wing_layer": REMI_WING_LAYER,
        "wing_zorder": REMI_WING_ZORDER,
        "wing_image": REMI_WING_IMAGE,
    }


    class RemiSprite(StatefulSprite):
        """
        Remi's body plus a separate wing image on the same layer.

        Wings track Remi's position and facing on every show/move/effect/hide.
        They default to a lower zorder so they stay behind other characters.
        """

        def __init__(
            self,
            wing_image=REMI_WING_IMAGE,
            wing_layer=REMI_WING_LAYER,
            wing_zorder=REMI_WING_ZORDER,
            **kwargs
        ):
            super(RemiSprite, self).__init__(**kwargs)

            self.wing_image = wing_image
            self.wing_tag = wing_image.split()[0]
            self.wing_layer = wing_layer
            self.wing_zorder = wing_zorder


        def _ensure_runtime_attrs(self):
            super(RemiSprite, self)._ensure_runtime_attrs()

            schema = STATEFUL_SPRITE_SCHEMAS.get(self.tag, {})

            if not hasattr(self, "wing_image"):
                self.wing_image = schema.get("wing_image", REMI_WING_IMAGE)

            if not hasattr(self, "wing_tag"):
                self.wing_tag = self.wing_image.split()[0]

            if not hasattr(self, "wing_zorder"):
                self.wing_zorder = schema.get("wing_zorder", REMI_WING_ZORDER)

            # Old saves kept wings on rear_sprites; move them to master.
            previous_layer = getattr(self, "wing_layer", None)

            if previous_layer is None or previous_layer == "rear_sprites":
                if previous_layer == "rear_sprites":
                    renpy.hide(self.wing_tag, layer="rear_sprites")

                self.wing_layer = schema.get("wing_layer", REMI_WING_LAYER)


        def show(
            self,
            at=None,
            transition=None,
            zorder=None,
            behind=None,
            reset=False,
            flip=False,
            wing_zorder=None,
            **changes
        ):
            self._sync_schema()

            if wing_zorder is not None:
                self.wing_zorder = wing_zorder

            return super(RemiSprite, self).show(
                at=at,
                transition=transition,
                zorder=zorder,
                behind=behind,
                reset=reset,
                flip=flip,
                **changes
            )


        def move(self, at, transition=None, zorder=None, wing_zorder=None):
            self._sync_schema()

            if wing_zorder is not None:
                self.wing_zorder = wing_zorder

            return super(RemiSprite, self).move(
                at,
                transition=transition,
                zorder=zorder,
            )


        def _sync_companions(self, show_arguments):
            self._ensure_runtime_attrs()

            wing_arguments = {
                "layer": self.wing_layer,
                "zorder": self.wing_zorder,
                # Keep wings behind Remi's body even when zorders match.
                "behind": [self.tag],
            }

            if "at_list" in show_arguments:
                wing_arguments["at_list"] = list(show_arguments["at_list"])

            elif (
                not renpy.showing(self.wing_tag, layer=self.wing_layer)
                and self.position is not None
            ):
                if isinstance(self.position, (list, tuple)):
                    at_list = list(self.position)
                else:
                    at_list = [self.position]

                at_list.append(sprite_facing(self.flipped))
                wing_arguments["at_list"] = at_list

            renpy.show(self.wing_image, **wing_arguments)


        def _hide_companions(self):
            self._ensure_runtime_attrs()
            renpy.hide(self.wing_tag, layer=self.wing_layer)
            # Clear any leftover wings from pre-migration saves.
            renpy.hide(self.wing_tag, layer="rear_sprites")


default remi = RemiSprite(
    tag="r",
    state_order=REMI_STATE_ORDER,
    defaults=REMI_DEFAULTS,
    compose=remi_compose,
)