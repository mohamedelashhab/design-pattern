from iterator.BrowseHistory import BrowseHistory
from iterator.Iterator import Iterator
if __name__ == '__main__':
    history: BrowseHistory = BrowseHistory[str]()
    history.push("a")
    history.push("b")
    history.push("c")
    history.push("d")
    history.push("e")
    history.push("f")

    iterator: Iterator = history.createIterator()

    while(iterator.hasNext()):
        url: str = iterator.current()
        print(url)
        iterator.next()
