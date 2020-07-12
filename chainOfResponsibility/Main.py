from chainOfResponsibility.Authenticator import Authenticator
from chainOfResponsibility.Compressor import Compressor
from chainOfResponsibility.Encryptor import Encryptor
from chainOfResponsibility.HttpRequest import HttpRequest
from chainOfResponsibility.Logger import Logger
from chainOfResponsibility.WebServer import WebServer

if __name__ == '__main__':
    encryptor = Encryptor(None)
    compressor = Compressor(encryptor)
    logger = Logger(compressor)
    authenticator = Authenticator(logger)
    server = WebServer(authenticator)
    server.handle(HttpRequest("admin", "1234"))