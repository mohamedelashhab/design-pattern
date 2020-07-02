from strategy.Compressor import Compressor


class PNGCompressor(Compressor):
    def compress(self, fileName: str) -> None:
        print("Compressing {} using PNG".format(fileName))