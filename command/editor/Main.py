from command.editor.BoldCommand import BoldCommand
from command.editor.History import History
from command.editor.HtmlDocument import HtmlDocument
from command.editor.UndoCommand import UndoCommand

if __name__ == '__main__':
    history = History()
    document = HtmlDocument()
    document.content = "Hello World"
    boldCommand = BoldCommand(history, document)
    boldCommand.execute()
    print(document.content)
    undoCommand = UndoCommand(history)
    undoCommand.execute()
    print(document.content)

