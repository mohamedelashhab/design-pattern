from visitor.HighlightOperation import HighlightOperation
from visitor.HtmlDocument import HtmlDocument
from visitor.HeadingNode import HeadingNode
from visitor.AnchorNode import AnchorNode
from visitor.PlaintextOperation import PlaintextOperation

if __name__ == '__main__':
    document = HtmlDocument()
    document.add(HeadingNode())
    document.add(AnchorNode())
    document.execute(HighlightOperation())
    document.execute(PlaintextOperation())