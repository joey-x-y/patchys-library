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
            lookup,
            layer="master",
        ):
            self.tag = tag
            self.state_order = tuple(state_order)
            self.defaults = defaults.copy()
            self.state = defaults.copy()
            self.lookup = lookup
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

            Raises a readable error if no matching flattened sprite exists.
            """

            if state is None:
                state = self.state

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

                renpy.show(
                    self._image_name(),
                    layer=self.layer,
                    at_list=at_list,
                )

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

            renpy.show(
                self._image_name(),
                layer=self.layer,
                at_list=at_list,
            )

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

            self._apply_transition(transition)

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

default flan = StatefulSprite(
    tag="f",

    state_order=(
        "expression",
        "dirty",
        "wings",
        "accessories",
    ),

    defaults={
        "expression": "neutral",
        "dirty": False,
        "wings": "default",
        "accessories": True,
    },

    lookup={
        # Default
        ("neutral", False, "default", True): "f neutral",
        ("smile",   False, "default", True): "f smile",

        # Dirty
        ("neutral", True, "default", True): "f neutral dirty",
        ("smile",   True, "default", True): "f smile dirty",

        # No wings
        ("neutral", False, "none", True): "f neutral nowing",
        ("smile",   False, "none", True): "f smile nowing",

        # Mid wings, accessories still present
        ("neutral", False, "mid", True): "f neutral midwing",
        ("smile",   False, "mid", True): "f smile midwing",

        # No accessories, default wings
        ("neutral", False, "default", False): "f neutral noacc",
        ("smile",   False, "default", False): "f smile noacc",

        # No accessories, mid wings
        ("neutral", False, "mid", False): "f neutral noacc midwing",
        ("smile",   False, "mid", False): "f smile noacc midwing",
    },
)


################################################################################
## pat
################################################################################

default pat = StatefulSprite(
    tag="p",

    state_order=(
        "expression",
        "hat",
        "magic",
    ),

    defaults={
        "expression": "neutral",
        "hat": True,
        "magic": False,
    },

    lookup={
        # Default
        ("neutral", True, False): "p neutral",
        ("smile",   True, False): "p smile",
        ("angry",   True, False): "p angry",

        # Magic
        ("neutral", True, True): "p neutral magic",
        ("smile",   True, True): "p smile magic",
        ("angry",   True, True): "p angry magic",

        # No hat
        ("neutral", False, False): "p neutral nohat",
        ("smile",   False, False): "p smile nohat",
        ("angry",   False, False): "p angry nohat",

        # No hat and magic
        ("neutral", False, True): "p neutral nohat magic",
        ("smile",   False, True): "p smile nohat magic",
        ("angry",   False, True): "p angry nohat magic",
    },
)


################################################################################
## REMI
################################################################################

default remi = StatefulSprite(
    tag="r",

    state_order=(
        "expression",
        "dirty",
        "accessories",
    ),

    defaults={
        "expression": "neutral",
        "dirty": False,
        "accessories": True,
    },

    lookup={
        # Default
        ("neutral", False, True): "r neutral",

        # Dirty
        ("neutral", True, True): "r neutral dirty",
        ("hunt",    True, True): "r hunt dirty",

        # No accessories
        ("neutral", False, False): "r neutral noacc",
    },
)