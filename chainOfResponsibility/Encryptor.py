from chainOfResponsibility.Handler import Handler


class Encryptor(Handler):
    def __init__(self, _next: Handler):
        super(Encryptor, self).__init__(_next)

    def doHandle(self, request) -> bool:
        print("Encryption")
        return False