from Template.Task import Task


class TransferMoneyTask(Task):
    def _doExecute(self) -> None:
        print("Transfer Money")