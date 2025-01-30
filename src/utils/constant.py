from pathlib import Path
# curent directory
current_path = Path(__file__).parents[1]
# Data directory
data_directory = current_path/'data'
# file in the directory
pdf_path = data_directory/"The-Gale-Encyclopedia-of-Medicine-3rd-Edition-staibabussalamsula.ac_.id_.pdf"

# print(db_path)
db_directory = current_path / 'vectorstore/'
DB_FAISS_PATH =  current_path / "vectorstore/db_faissss"
# print(db_directory)
db_file = db_directory / "db_faissss"
print(db_file)

#