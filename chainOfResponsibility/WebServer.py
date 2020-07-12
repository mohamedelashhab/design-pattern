from chainOfResponsibility.Handler import Handler


class WebServer(object):
    def __init__(self, handler: Handler):
        self.__handler = handler

    def handle(self, request) -> None:
        self.__handler.handle(request)

