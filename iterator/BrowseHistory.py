from iterator.Iterator import Iterator
from typing import TypeVar, Generic, List

T = TypeVar('T')
class BrowseHistory(Generic[T]):
    def __init__(self):
        self.__urls: List[T] = []

    def push(self, url: T) -> None:
        self.__urls.append(url)

    def pop(self) -> T:
        if len(self.__urls) > 0:
            self.__urls.pop()
        else: return None

    @property
    def urls(self) -> List[T]:
        return self.__urls



    class ListIterator(Iterator):

        def __init__(self, history):
            self.__history = history
            self.__index =0

        def hasNext(self) -> bool:
            return self.__index < len(self.__history.urls)

        def current(self) -> T:
            if self.__index <= len(self.__history.urls):
                return self.__history.urls[self.__index]
            return ''

        def next(self) -> None:
            if(self.hasNext()):
                self.__index += 1


    def createIterator(self) -> Iterator:
        return self.ListIterator(self)
