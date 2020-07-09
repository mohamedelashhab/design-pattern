from mediator.Button import Button
from mediator.DialogBox import DialogBox
from mediator.ListBox import ListBox
from mediator.TextBox import TextBox


class ArticlesDialogBox(DialogBox):

    def __init__(self):
        self.__articlesListBox = ListBox(self)
        self.__titleTextBox = TextBox(self)
        self.__saveButton = Button(self)


    def simulateUserInteraction(self):
        self.__articlesListBox.selection = "A1"
        # self.__titleTextBox.text = ""
        print("TextBox: {}".format(self.__titleTextBox.text))
        print("Button:  {}".format(self.__saveButton.isEnabled))

    def changed(self, control):
        if isinstance(control, ListBox):
            self.__titleTextBox.text = "selection"
            self.__saveButton.isEnabled = True
        elif isinstance(control, TextBox):
            content = self.__titleTextBox.text
            isEmpty = (not content or content is None)
            self.__saveButton.isEnabled = not isEmpty
