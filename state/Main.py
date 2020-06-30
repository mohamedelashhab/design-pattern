from state.Canvas import Canvas
from state.SelectionTool import SelectionTool
from state.BrushTool import BrushTool
if __name__ == '__main__':
    canvas: Canvas = Canvas()
    canvas.currentTool = BrushTool()
    canvas.mouseUp()
    canvas.mouseDown()

    canvas: Canvas = Canvas()
    canvas.currentTool = SelectionTool()
    canvas.mouseUp()
    canvas.mouseDown()