from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_PATH = "chroma_db"

def get_embedding():

    return OpenAIEmbeddings(
        model="text-embedding-3-small"
    )


def load_db():

    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding()
    )