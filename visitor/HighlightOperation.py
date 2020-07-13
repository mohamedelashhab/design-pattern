from typing import overload

from visitor.AnchorNode import AnchorNode
from visitor.HeadingNode import HeadingNode
from visitor.Operation import Operation

class HighlightOperation(Operation):
    def apply(self, node) -> None:
        print("Highlight-{}".format(node.__class__.__name__))
