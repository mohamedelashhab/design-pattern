
#Observable
from abc import ABC

from observer.Observer import Observer


class Subject(ABC):
    def __init__(self):
        self.__observers = []

    def addObserver(self, observer: Observer):
        self.__observers.append(observer)

    def removeObserver(self, observer: Observer):
        self.__observers.remove(observer)

    def notifyObservers(self):
        for observer in self.__observers:
            observer.update()

