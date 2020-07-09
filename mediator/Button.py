from .UIControl import DialogBox
from mediator.UIControl import UIControl


class Button(UIControl):
    def __init__(self, owner: DialogBox):
        self.__isEnabled = False
        super(Button, self).__init__(owner)

    @property
    def isEnabled(self):
        return self.__isEnabled

    @isEnabled.setter
    def isEnabled(self, enabled: bool):
        self.__isEnabled = enabled
        self._owner.changed(self)
