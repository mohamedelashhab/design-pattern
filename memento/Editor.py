from memento.EditorState import EditorState


class Editor():
    def __init__(self):
        self.__content = ''

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        self.__content = value

    def createState(self) -> EditorState:
        return EditorState(self.__content)

    def restore(self, state: EditorState) -> EditorState:
        self.content = state.content



