from chainOfResponsibility.Handler import Handler


class Compressor(Handler):
    def __init__(self, _next):
        super(Compressor, self).__init__(_next)

    def doHandle(self, request) -> bool:
        print("Compress")
        return False