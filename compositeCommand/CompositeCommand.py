from compositeCommand.Command import Command


class CompositeCommand(Command):
    def __init__(self):
        self.__commands = []

    def add(self, command: Command):
        self.__commands.append(command)

    def execute(self) -> None:
        for command in self.__commands:
            command.execute()
