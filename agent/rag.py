# agent/rag.py


class RAGIndex:
    def __init__(self, vector_db_client):
        self.vector_db_client = vector_db_client

    def index_document(self, doc_id: str, text: str, metadata: dict):
        """Ingest document (text -> embeddings -> store)."""
        raise NotImplementedError("index_document is not yet implemented")

    def query(self, query_text: str, top_k: int = 5) -> list:
        """Return list of {id, text, score, metadata} relevant chunks."""
        raise NotImplementedError("query is not yet implemented")

    def delete_doc(self, doc_id: str):
        """Remove doc from index if needed."""
        raise NotImplementedError("delete_doc is not yet implemented")
