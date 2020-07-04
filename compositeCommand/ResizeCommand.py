from compositeCommand.Command import Command


class ResizeCommand(Command):
    def execute(self) -> None:
        print("resize image")
