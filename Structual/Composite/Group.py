from .Component import Component

class Group(Component):
    def __init__(self):
        self.__objects = []

    def render(self):
        for object in self.__objects:
            object.render()

    def add(self, shape):
        self.__objects.append(shape)
