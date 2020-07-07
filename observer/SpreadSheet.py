from observer.DataSource import DataSource
from observer.Observer import Observer


class SpreadSheet(Observer):
    def __init__(self, dataSource: DataSource):
        self.__dataSource = dataSource

    def update(self) -> None:
        print("sheet notified " + str(self.__dataSource.getValue()))