from chainOfResponsibility.Handler import Handler
from chainOfResponsibility.HttpRequest import HttpRequest


class Authenticator(Handler):
    def __init__(self, _next):
        super(Authenticator, self).__init__(_next)
    def doHandle(self, request: HttpRequest) -> bool:
        print("Authentication")
        if  request.username == "admin" and request.password == "1234":
            return False
        return True