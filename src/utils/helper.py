from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def pdf_loader(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    print("Harsh")
    return documents

def split_text(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=25)
    text_chunks = text_splitter.split_documents(text)
    return text_chunks





