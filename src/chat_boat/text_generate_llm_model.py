import os
import time

from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, HuggingFaceEmbeddings


def load_llm(repo_id, hf_token):
    """Load the LLM with error handling and retries."""
    for attempt in range(3):
        try:
            llm = HuggingFaceEndpoint(
                repo_id=repo_id,
                task="text-generation",
                temperature=0.5,
                model_kwargs={"max_length": 512},
                huggingfacehub_api_token=hf_token
            )
            return llm
        except Exception as e:
            print(f"Attempt {attempt + 1}: Error loading LLM - {e}")
            time.sleep(30)
    raise RuntimeError("Failed to load LLM after multiple attempts")



def load_faiss(db_path, embedding_model):
    """Load the FAISS database."""
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"FAISS database not found at {db_path}. Make sure it's created properly.")
    try:
        return FAISS.load_local(db_path, embedding_model, allow_dangerous_deserialization=True)
    except Exception as e:
        raise RuntimeError(f"Error loading FAISS database: {e}")


def create_qa_chain(llm, db):
    """Create the RetrievalQA chain."""
    custom_prompt_template = PromptTemplate(
        template="""Use the following context to answer the question accurately.

        Context: {context}
        Question: {question}

        Provide a direct response without any extra conversation.
        """,
        input_variables=["context", "question"]
    )
    try:
        return RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=db.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True,
            chain_type_kwargs={'prompt': custom_prompt_template}
        )
    except Exception as e:
        raise RuntimeError(f"Error creating RetrievalQA chain: {e}")

def ask_question(qa_chain, user_query):
    """Query the QA chain and return the result."""
    if not user_query.strip():
        raise ValueError("No question provided.")
    try:
        response = qa_chain.invoke({"query": user_query})
        return response["result"], response["source_documents"]
    except Exception as e:
        raise RuntimeError(f"Error while querying the model: {e}")



