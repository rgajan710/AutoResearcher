from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import WebBaseLoader

class VectorDBTool:
    def __init__(self):
        self.loader = WebBaseLoader("https://arxiv.org")
        self.docs = self.loader.load()
        self.db = FAISS.from_documents(self.docs, OpenAIEmbeddings())

    def search(self, query):
        return self.db.similarity_search(query, k=5)