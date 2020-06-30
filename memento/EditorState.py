

class EditorState():
    def __init__(self, content):
        self.__content = content

    @property
    def content(self):
        return self.__content

    def __str__(self):
        return str(self.__content)

