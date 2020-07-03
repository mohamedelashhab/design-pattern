from command.Command import Command



class Button():
    def __init__(self, command: Command):
        self.__command: Command = command

    def click(self) -> None:
        self.__command.execute()