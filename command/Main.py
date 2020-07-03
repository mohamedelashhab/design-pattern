from command.AddCustomerCommand import AddCustomerCommand
from command.Button import Button
from command.CustomerService import CustomerService

if __name__ == '__main__':
    service: CustomerService = CustomerService()
    command: AddCustomerCommand = AddCustomerCommand(service= service)
    button: Button = Button(command=command)
    button.click()
