from documents import Document, Report, Invoice, Contract, NullDocument

class DocumentFactory:
    @staticmethod
    def create(doc_type: str) -> Document:
        doc_type = doc_type.lower()
        match doc_type:
            case "report":
                return Report()
            case "invoice":
                return Invoice()
            case "contract":
                return Contract()
            case _:
                return NullDocument()