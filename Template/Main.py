from Template.GenerateReportTask import GenerateReportTask
from Template.Task import Task
from Template.TransferMoneyTask import TransferMoneyTask

if __name__ == '__main__':
    task: Task = TransferMoneyTask()
    task.execute()
    task = GenerateReportTask()
    task.execute()