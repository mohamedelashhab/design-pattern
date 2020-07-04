from typing import List

from command.editor.UndoableCommand import UndoableCommand


class History():
    def __init__(self):
        self.__commands = []

    def push(self, command: UndoableCommand) -> None:
        self.__commands.append(command)

    def pop(self) -> UndoableCommand:
        return self.__commands.pop()

    def size(self) -> int:
        return len(self.__commands)
