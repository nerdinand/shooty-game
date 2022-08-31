import numpy.typing as npt
from gym import spaces


BUTTON_FORWARD = "forward"
BUTTON_LEFT = "left"
BUTTON_BACKWARD = "backward"
BUTTON_RIGHT = "right"

BUTTON_RELOAD = "reload"
BUTTON_SHOOT = "shoot"

BUTTON_LOOK_LEFT = "look_left"
BUTTON_LOOK_RIGHT = "look_right"


class Buttons:
    ALL_BUTTONS: list[str] = [
        BUTTON_FORWARD,
        BUTTON_LEFT,
        BUTTON_BACKWARD,
        BUTTON_RIGHT,
        BUTTON_RELOAD,
        BUTTON_SHOOT,
        BUTTON_LOOK_LEFT,
        BUTTON_LOOK_RIGHT,
    ]

    def __init__(self, allow_reload: bool) -> None:
        self.buttons: list[str] = Buttons.ALL_BUTTONS.copy()
        if not allow_reload:
            self.buttons.remove(BUTTON_RELOAD)

    def space(self) -> spaces.multi_binary.MultiBinary:
        return spaces.MultiBinary(len(self.buttons))

    def __is_button_allowed(self, button: str) -> bool:
        return button in self.buttons

    def is_button_pushed(self, actions: npt.NDArray, button: str) -> bool:
        return (
            self.__is_button_allowed(button)
            and actions[self.buttons.index(button)] == 1
        )
