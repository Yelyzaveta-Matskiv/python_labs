from factory import DocumentFactory

def process_document(doc_type: str):
    document = DocumentFactory.create(doc_type)
    print(document.render())

if __name__ == "__main__":
    doc_types = ["report", "invoice", "contract", "memo"]

    for doc_type in doc_types:
        process_document(doc_type)


        