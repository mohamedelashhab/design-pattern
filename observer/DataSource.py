from observer.Subject import Subject


class DataSource(Subject):

    def __init__(self):
        self.__value = None
        super(DataSource, self).__init__()

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        self.notifyObservers()

    def getValue(self):
        return self.__value



