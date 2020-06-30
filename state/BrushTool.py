from state.Tool import Tool


class BrushTool(Tool):
    def mouseUp(self):
        print("Brush mouse up")

    def mouseDown(self):
        print("Brush mouse down")