from visitor.HtmlNode import HtmlNode


class HeadingNode(HtmlNode):
    def execute(self, operation) -> None:
        operation.apply(self)

