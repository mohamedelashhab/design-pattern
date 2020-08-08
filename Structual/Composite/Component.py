from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def render(self):
        raise NotImplementedError