# chroma-llm-chatbot

## Getting Started

* Create virtual environment

```shell
python3 -m venv ./venv
```

* Activate virtual environment

```shell
source ./.venv/bin/activate
```

* Bootstrap

```shell
sh bootstrap.sh
```

* Source .env

```shell
source .env
```

## `models` folder

Put models inside this folder.

Choose Lightweight LLM (CPU-Only). Use GGUF models with llama.cpp or 
Python bindings like llama-cpp-python.

Recommended Model:
- Phi-2 (2.7B) – very capable and CPU-friendly.
- TinyLlama (1.1B) – super lightweight.

## `documents` folder

Put your files inside this folder. It will be used to answer your queries.

## Create/Update embeddings

After adding/updating files in `documents` folder, run the following command
to create/update embeddings in the chroma vector database.

```shell
python3 src/embedding.py
```
