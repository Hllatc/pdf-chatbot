from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.database import get_embedding
from langchain_chroma import Chroma

from dotenv import load_dotenv
from app.services.llm import get_llm
from app.services.prompt import build_prompt

load_dotenv()


def load_pdf(file_path):

    loader = PyPDFLoader(file_path)

    return loader.load()


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.split_documents(documents)


CHROMA_PATH = "chroma_db"

def add_pdf_to_db(file_path):

    documents = load_pdf(file_path)
    chunks = split_documents(documents)

    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding()
    )

    db.add_documents(chunks)

    return len(chunks)

from app.database import load_db

def retrieve(question):

    db = load_db()

    docs = db.similarity_search(
        question,
        k=4
    )

    return docs



def ask_pdf(question):
    docs = retrieve(question)

    context = ""

    sources = []

    for doc in docs:

        page = doc.metadata.get("page", "?")

        sources.append(page)

        context += f"""
    Page {page}

    {doc.page_content}

    """
        
    prompt = build_prompt(context, question)
    
    llm = get_llm()
    
    response = llm.invoke(prompt)

    return {
    "answer": response.content,
    "sources": list(set(sources))
}