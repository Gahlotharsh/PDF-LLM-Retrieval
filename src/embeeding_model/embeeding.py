from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from src.utils.constant import DB_FAISS_PATH


def embedding_model():
    model = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")
    return model


def vector(text_chunks, model):
    db = FAISS.from_documents(text_chunks, model)
    db.save_local(DB_FAISS_PATH)



