# PDF Processing & Retrieval System Using LLM and FAISS

This project extracts text from PDF documents, processes them into chunks, embeds the text into a FAISS vector database, and enables intelligent search using a Large Language Model (LLM).

## Features

- **PDF Parsing**: Extracts text from PDF documents.
- **Text Chunking**: Splits text into manageable segments for better retrieval.
- **FAISS Vector Store**: Stores embeddings for fast similarity search.
- **LLM-powered Q&A**: Uses a Hugging Face model to answer questions based on the PDF content.
- **Custom Prompting**: Provides precise and direct responses using a structured prompt.

## Installation

### Clone the Repository

```bash
git clone git@github.com:Gahlotharsh/PDF-LLM-Retrieval.git
cd PDF-LLM-Retrieval

## Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

## Install Dependencies
pip install -r requirements.txt

### Usage
## Load and Process a PDF
# Load and Process a PDF
## Run the script:
python main.py
## Query the Model for Answers:
from src.chat_boat.text_generate_llm_model import ask_question
response, sources = ask_question(qa_chain, "What is heart disease?")
print(response)

