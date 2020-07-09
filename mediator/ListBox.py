from .UIControl import DialogBox
from mediator.UIControl import UIControl


class ListBox(UIControl):
    def __init__(self, owner: DialogBox):
        self.__selection = ''
        super(ListBox, self).__init__(owner)

    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, selection):
        self.__selection = selection
        self._owner.changed(self)

