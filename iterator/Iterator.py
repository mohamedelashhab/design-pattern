from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def hasNext(self) -> bool: raise NotImplementedError

    @abstractmethod
    def current(self) -> str: raise NotImplementedError

    @abstractmethod
    def next(self) -> str: raise NotImplementedError