from compositeCommand.Command import Command
from compositeCommand.CustomerService import CustomerService


class AddCustomerCommand(Command):
    def __init__(self, service: CustomerService):
        self.__service = service

    def execute(self) -> None:
        self.__service.addCustomer()
