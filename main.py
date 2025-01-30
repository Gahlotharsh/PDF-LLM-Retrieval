from src.embeeding_model.embeeding import embedding_model, vector
from src.chat_boat.text_generate_llm_model import load_llm, load_faiss, create_qa_chain, ask_question
from src.utils.constant import DB_FAISS_PATH

from src.utils.helper import pdf_loader, split_text
from src.utils.constant import pdf_path
import os
hf_token = os.getenv("HF_TOKEN")

def pdf_runner():
    documents = pdf_loader(pdf_path)
    # print(data_directory)
    text_chunks = split_text(documents)
    return text_chunks


if __name__=="__main__":

    #1
    repo_id = "deepseek-ai/DeepSeek-R1"
    text_chunk=pdf_runner()
    model = embedding_model()
    vector(text_chunk,model)



    #2
    llm=load_llm(repo_id,hf_token)
    loaded_db = load_faiss(DB_FAISS_PATH, model)
    qa_chain = create_qa_chain(llm,loaded_db)

    user_query = input("Write your question here: ").strip()
    if not user_query:
        print("Please enter a valid question.")
    result, sources = ask_question(qa_chain, user_query)

    print("\nRESULT:", result)
    print("\nSOURCE DOCUMENTS:", sources)








