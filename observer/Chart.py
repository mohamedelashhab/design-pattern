from observer.DataSource import DataSource
from observer.Observer import Observer


class Chart(Observer):
    def __init__(self, dataSource: DataSource):
        self.__dataSource = dataSource

    def update(self) -> None:
        print("chart notified " + str(self.__dataSource.getValue()))