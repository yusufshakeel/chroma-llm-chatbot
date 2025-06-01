from llama_cpp import Llama
from env_config import MODEL_PATH, NUMBER_OF_MOST_SIMILAR_DOCUMENTS_TO_RETRIEVE, CONTEXT_SIZE, NUMBER_OF_THREADS
from vector_store import collection, emb_fn

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=CONTEXT_SIZE,
    n_threads=NUMBER_OF_THREADS
)


def get_context(query: str):
    query_embedding = emb_fn([query])[0]
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=NUMBER_OF_MOST_SIMILAR_DOCUMENTS_TO_RETRIEVE
    )
    relevant_chunks = [doc for sublist in results["documents"] for doc in sublist]
    return "\n\n".join(relevant_chunks)


def main():
    try:
        while True:
            query = input("Query: ").strip()
            context = get_context(query)

            prompt = f"You are a helpful assistant. \
            Use the following context to answer the user's \
            question accurately and concisely. \
            The contexts and user's questions are delimited by #####. \
            \nContext:\n\
            #####\n\
            {context}\n\
            #####\n\
            \nQuestion:\n\
            #####\n\
            {query}\n\
            #####\n\
            Answer: "

            response = llm(prompt)
            print("Response: ", response["choices"][0]["text"])
            print("\n\n")
    except KeyboardInterrupt:
        print("\n\nExiting... Bye!")


if __name__ == "__main__":
    main()
