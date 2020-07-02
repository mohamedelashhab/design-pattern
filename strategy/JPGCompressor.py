from strategy.Compressor import Compressor
class JPGCompressor(Compressor):
    def compress(self, fileName: str) -> None:
        print("Compressing {} using JPG".format(fileName))