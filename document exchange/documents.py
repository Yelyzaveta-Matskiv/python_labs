from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Report(Document):
    def render(self) -> str:
        return "Report: Quarterly performance overview."


class Invoice(Document):
    def render(self) -> str:
        return "Invoice: Payment due for services rendered."


class Contract(Document):
    def render(self) -> str:
        return "Contract: Legal agreement between parties."


class NullDocument(Document):
    def render(self) -> str:
        return "Unknown document type. Nothing to render."