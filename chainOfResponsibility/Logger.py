from chainOfResponsibility.Handler import Handler


class Logger(Handler):

    def __init__(self, _next):
        super(Logger, self).__init__(_next)

    def doHandle(self, request) -> bool:
        print("Log")
