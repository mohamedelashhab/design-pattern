from command.Command import Command
from command.CustomerService import CustomerService


class AddCustomerCommand(Command):
    def __init__(self, service):
        self.__service: CustomerService = service

    def execute(self):
        self.__service.addCustomer()
