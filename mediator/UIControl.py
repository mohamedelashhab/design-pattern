from mediator.DialogBox import DialogBox


class UIControl:
    def __init__(self, owner: DialogBox):
        self._owner = owner
