from abc import ABC, abstractmethod



class HtmlNode(ABC):

    @abstractmethod
    def execute(self, operation) -> None:
        raise NotImplementedError