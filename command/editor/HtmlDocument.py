class HtmlDocument():

    def __init__(self):
        self.__content = ''

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    def makeBold(self):
        self.__content = "<b>" + self.__content + "</b>"



