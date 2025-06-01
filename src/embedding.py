from vector_store import emb_fn, collection
from document_loader import load_documents
from text_splitter import split_text
from pathlib import Path

DOCUMENTS_DIR = Path(__file__).resolve().parent.parent / "documents"

documents = load_documents(DOCUMENTS_DIR)

for document in documents:
    chunks = split_text(document["text"])
    for index, chunk in enumerate(chunks):
        collection.upsert(
            ids=[f"{document['id']}-chunk-{index}"],
            documents=[chunk],
            embeddings=[emb_fn([chunk])[0]]
        )
