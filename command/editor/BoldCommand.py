from command.editor.History import History
from command.editor.HtmlDocument import HtmlDocument
from command.editor.UndoableCommand import UndoableCommand


class BoldCommand(UndoableCommand):
   def __init__(self, history: History, document: HtmlDocument):
       self.__history = history
       self.__document = document
       self.__prevContent = ''

   def unexecute(self) -> None:
       self.__document.content = self.__prevContent

   def execute(self) -> None:
       self.__prevContent = self.__document.content
       self.__document.makeBold()
       self.__history.push(self)

