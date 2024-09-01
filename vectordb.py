from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from scraping import findreplst
import nest_asyncio

nest_asyncio.apply()

url = "https://en.wikipedia.org/wiki/List_of_current_members_of_the_United_States_House_of_Representatives"

replsts = findreplst(url)

persist_directory = './chroma_politics/'


loader = WebBaseLoader(replsts)
loader.requests_per_second = 2
docs = loader.aload()
print(docs[0])

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1500,
    chunk_overlap = 150
)
embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

splits = text_splitter.split_documents(docs)

vectordb = Chroma.from_documents(
    documents=splits,
    embedding=embedding,
    persist_directory=persist_directory
)
