from abc import ABC, abstractmethod

from Template.AuditTrail import AuditTrail


class Task(ABC):
    def __init__(self):
        self.__auditTrail = AuditTrail()

    def execute(self) -> None:
        self.__auditTrail.record()
        self._doExecute()

    @abstractmethod
    def _doExecute(self) -> None:
            raise NotImplementedError