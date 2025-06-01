def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def extract_text(file_path):
    ext = file_path.suffix.lower()
    if ext == ".txt":
        return load_txt(file_path)
    return ""


def load_documents(documents_dir):
    documents = []
    for file_path in documents_dir.glob("*"):
        print(f"Reading file: {file_path}")
        if file_path.is_file():
            text = extract_text(file_path)
            if text.strip():
                documents.append({
                    "id": file_path.name,
                    "text": text.strip(),
                })
    return documents
