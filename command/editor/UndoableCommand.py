from abc import abstractmethod

from command.editor.Command import Command


class UndoableCommand(Command):
    @abstractmethod
    def unexecute(self) -> None:
        raise NotImplementedError
