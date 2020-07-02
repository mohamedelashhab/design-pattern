from strategy.BlackAndWhiteFilter import BlackAndWhiteFilter
from strategy.ImageStorage import ImageStorage
from strategy.JPGCompressor import JPGCompressor
from strategy.PNGCompressor import PNGCompressor

if __name__ == '__main__':
    imageStorage = ImageStorage()
    imageStorage.store("football", JPGCompressor(), BlackAndWhiteFilter())
    imageStorage.store("dog", PNGCompressor(), BlackAndWhiteFilter())