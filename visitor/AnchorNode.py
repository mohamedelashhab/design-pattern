from visitor.HtmlNode import HtmlNode


class AnchorNode(HtmlNode):
    def execute(self, operation) -> None:
        operation.apply(self)

