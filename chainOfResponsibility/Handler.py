from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, _next):
        self.__next = _next

    @abstractmethod
    def doHandle(self, request)->bool:
        raise NotImplementedError

    def handle(self, request):
        if self.doHandle(request): return
        if self.__next is not None: self.__next.handle(request)

