class HtmlDocument(object):
    def __init__(self):
        self.__nodes = []

    def add(self, node) -> None:
        self.__nodes.append(node)

    def execute(self, operation):
        for node in self.__nodes:
            node.execute(operation)