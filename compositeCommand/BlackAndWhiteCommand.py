from compositeCommand.Command import Command


class BlackAndWhiteCommand(Command):
    def execute(self) -> None:
        print("B & W Filter")