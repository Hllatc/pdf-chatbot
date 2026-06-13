from langchain_chroma import Chroma
CHROMA_PATH = "chroma_db"

from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding():

    return HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-base"
    )


def load_db():

    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding()
    )