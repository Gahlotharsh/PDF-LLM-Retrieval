PDF Processing & Retrieval System Using LLM and FAISS

This project extracts text from PDF documents, processes them into chunks, embeds the text into a FAISS vector database, and enables intelligent search using a Large Language Model (LLM).

Features

PDF Parsing: Extracts text from PDF documents.

Text Chunking: Splits text into manageable segments for better retrieval.

FAISS Vector Store: Stores embeddings for fast similarity search.

LLM-powered Q&A: Uses a Hugging Face model to answer questions based on the PDF content.

Custom Prompting: Provides precise and direct responses using a structured prompt.

Installation

Clone the Repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

Install Dependencies
pip install -r requirements.txt

Usage

Load and Process a PDF

Modify the pdf_path in constant.py to specify the target PDF file.

Run the script:
python main.py

Generate Embeddings and Store in FAISS

Modify embedding.py to process the PDF into FAISS.

Query the Model for Answers
from src.chat_boat.text_generate_llm_model import ask_question
response, sources = ask_question(qa_chain, "What is heart disease?")
print(response)