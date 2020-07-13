from abc import ABC, abstractmethod
from typing import overload

from visitor.AnchorNode import AnchorNode
from visitor.HeadingNode import HeadingNode


class Operation(ABC):
    @abstractmethod
    def apply(self, node) -> None:
        raise NotImplementedError