from compositeCommand.BlackAndWhiteCommand import BlackAndWhiteCommand
from compositeCommand.CompositeCommand import CompositeCommand
from compositeCommand.ResizeCommand import ResizeCommand

if __name__ == '__main__':
    composite = CompositeCommand()
    composite.add(ResizeCommand())
    composite.add(BlackAndWhiteCommand())
    composite.execute()
    composite.execute()