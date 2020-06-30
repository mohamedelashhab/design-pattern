from abc import ABC, abstractmethod

class Tool(ABC):
    @abstractmethod
    def mouseUp(self): raise NotImplementedError

    @abstractmethod
    def mouseDown(self): raise NotImplementedError