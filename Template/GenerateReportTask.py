from Template.Task import Task


class GenerateReportTask(Task):

    def _doExecute(self) -> None:
        print("Generate Report")