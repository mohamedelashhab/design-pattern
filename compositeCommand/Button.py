from command.Command import Command


class Button():
    def __init__(self, command: Command):
        self.__command = command

    def click(self):
        self.__command.execute()
