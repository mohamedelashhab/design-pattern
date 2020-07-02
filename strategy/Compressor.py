from abc import ABC, abstractmethod


class Compressor(ABC):
    @abstractmethod
    def compress(self, fileName: str) -> None :
        raise NotImplementedError