from mediator.UIControl import UIControl
from .UIControl import DialogBox

class TextBox(UIControl):
    def __init__(self, owner: DialogBox):
        self.__text = ''
        super(TextBox, self).__init__(owner)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text
        self._owner.changed(self)