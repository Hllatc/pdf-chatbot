from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

import shutil

from app.rag import add_pdf_to_db

app = FastAPI()

@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    path = f"app/uploads/{file.filename}"

    with open(path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    chunks = add_pdf_to_db(path)

    return {
        "message": "PDF indexed",
        "chunks": chunks
    }

from app.schemas import QuestionRequest
from app.rag import ask_pdf

@app.post("/ask")
def ask(request: QuestionRequest):

    return ask_pdf(
        request.question
    )