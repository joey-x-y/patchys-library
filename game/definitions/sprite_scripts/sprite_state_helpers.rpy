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

            # Remember the last position used by move() or show(position=...).
            self.position = None


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


        def _image_name(self, state=None):
            """
            Returns the Ren'Py image name for a given state.

            Uses compose() when provided (e.g. layeredimages), otherwise lookup.
            """

            if state is None:
                state = self.state

            if self.compose is not None:
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

            if reset:
                proposed_state = self.defaults.copy()
            else:
                proposed_state = self.state.copy()

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

            show_arguments = {
                "layer": self.layer,
            }

            if zorder is not None:
                show_arguments["zorder"] = zorder

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

            self.position = at

            if renpy.showing(self.tag, layer=self.layer):

                if isinstance(at, (list, tuple)):
                    at_list = list(at)
                else:
                    at_list = [at]

                at_list.append(sprite_facing(self.flipped))

                show_arguments = {
                    "layer": self.layer,
                    "at_list": at_list,
                }

                if zorder is not None:
                    show_arguments["zorder"] = zorder

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


        def hunt(self, value=True, transition=None):
            return self.show(
                hunt=value,
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
        "begin": "begin",
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
            "noacc" if not state["accessories"] else "clean",
            expression,
        ]

        if state.get("blush"):
            parts.append("blushing")
        else:
            parts.append("noeffect")

        if state["dirty"]:
            parts.append("dirty")
        else:
            parts.append("none")

        return " ".join(parts)


default flan = StatefulSprite(
    tag="f",

    state_order=(
        "expression",
        "dirty",
        "wings",
        "accessories",
        "blush",
    ),

    defaults={
        "expression": "neutral",
        "dirty": False,
        "wings": "default",
        "accessories": True,
        "blush": False,
    },

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

        if state["magic"] and not state["hat"]:
            base = "magicnohat"
        elif state["magic"]:
            base = "magic"
        elif not state["hat"]:
            base = "nohat"
        else:
            base = "base"

        parts = [
            "p",
            base,
            expression,
        ]

        if state["blush"]:
            parts.append("blushing")
        else:
            parts.append("noeffect")

        return " ".join(parts)


default pat = StatefulSprite(
    tag="p",

    state_order=(
        "expression",
        "hat",
        "magic",
        "blush",
    ),

    defaults={
        "expression": "neutral",
        "hat": True,
        "magic": False,
        "blush": False,
    },

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
        "holding_tear",
        "serious",
        "smile",
        "surprised",
    )

    REMI_WING_LAYER = "rear_sprites"

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

        if state["glove"] == "Off":
            parts.append("noglove")
        elif state["glove"] == "Blood":
            parts.append("bloody")
        else:
            parts.append("glove")

        if not state["hat"]:
            parts.append("nohat")
        else:
            parts.append("hat")

        if state["blush"]:
            parts.append("blushing")
        else:
            parts.append("noeffect")

        if state["dirty"]:
            parts.append("dirty")
        else:
            parts.append("none")

        return " ".join(parts)


    class RemiSprite(StatefulSprite):
        """
        Remi's body plus a separate wing image on rear_sprites.

        Wings track Remi's position and facing on every show/move/effect/hide,
        but always display on the rear_sprites layer so they stay behind other
        characters on master.
        """

        def __init__(
            self,
            wing_image="r_wings",
            wing_layer=REMI_WING_LAYER,
            **kwargs
        ):
            super(RemiSprite, self).__init__(**kwargs)

            self.wing_image = wing_image
            self.wing_tag = wing_image.split()[0]
            self.wing_layer = wing_layer


        def _sync_companions(self, show_arguments):
            wing_arguments = {
                "layer": self.wing_layer,
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
            renpy.hide(self.wing_tag, layer=self.wing_layer)


default remi = RemiSprite(
    tag="r",

    state_order=(
        "expression",
        "hat",
        "glove",
        "dirty",
        "blush",
    ),

    defaults={
        "expression": "neutral",
        "hat": True,
        "glove": "On",
        "dirty": False,
        "blush": False,
    },

    compose=remi_compose,
)