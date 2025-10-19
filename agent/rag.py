# agent/rag.py

class RAGIndex:
    def __init__(self, vector_db_client):
        pass

    def index_document(self, doc_id: str, text: str, metadata: dict):
        """Ingest document (text -> embeddings -> store)"""

    def query(self, query_text: str, top_k: int = 5) -> list:
        """Return list of {id, text, score, metadata} relevant chunks"""

    def delete_doc(self, doc_id: str):
        """Remove doc from index if needed"""
