from abc import ABC, abstractmethod


class Filter(ABC):
    @abstractmethod
    def apply(self, fileName: str) -> None:
        raise NotImplementedError
