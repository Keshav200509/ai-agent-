"""Unit tests for agent/rag.py — RAGIndex class."""

from agent.rag import RAGIndex


def test_rag_index_init():
    """RAGIndex can be created with a vector_db_client."""
    idx = RAGIndex(vector_db_client=None)
    assert isinstance(idx, RAGIndex)


def test_index_document_stub():
    """index_document is a stub and returns None."""
    idx = RAGIndex(vector_db_client=None)
    result = idx.index_document("doc1", "hello world", {"author": "test"})
    assert result is None


def test_query_stub():
    """query is a stub and returns None."""
    idx = RAGIndex(vector_db_client=None)
    result = idx.query("search term", top_k=3)
    assert result is None


def test_delete_doc_stub():
    """delete_doc is a stub and returns None."""
    idx = RAGIndex(vector_db_client=None)
    result = idx.delete_doc("doc1")
    assert result is None
