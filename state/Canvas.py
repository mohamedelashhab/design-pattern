from state.Tool import Tool
class Canvas():
    def __init__(self):
        self.__currentTool: Tool

    @property
    def currentTool(self) -> Tool:
        return self.__currentTool

    @currentTool.setter
    def currentTool(self, currentTool: Tool) -> None:
        self.__currentTool = currentTool

    def mouseUp(self):
        self.__currentTool.mouseUp()

    def mouseDown(self):
        self.__currentTool.mouseDown()