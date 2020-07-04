from command.editor.Command import Command
from command.editor.History import History


class UndoCommand(Command):

    def __init__(self, history: History):
        self.__history = history

    def execute(self) -> None:
        if self.__history.size() > 0:
            self.__history.pop().unexecute()
