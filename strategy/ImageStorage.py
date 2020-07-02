from strategy.Compressor import Compressor
from strategy.Filter import Filter


class ImageStorage():
    def store(self, fileName: str, compressor: Compressor, filter: Filter) -> None:
        compressor.compress(fileName)
        filter.apply(fileName)

