from typing import Dict, Any, List, Optional

class KnowledgeRetriever:
    """Document Ingestion, Chunking, and Vector Search Retrieval Pipeline."""

    def __init__(self):
        self.documents_index: List[Dict[str, Any]] = [
            {
                "id": "doc-1",
                "title": "Enterprise Master Services Agreement - ABC Corp",
                "chunk": "Termination clause: Either party may terminate with 60 days written notice prior to annual renewal date of November 14.",
                "metadata": {"type": "contract", "customer": "ABC Corp", "arr": 340000}
            },
            {
                "id": "doc-2",
                "title": "SLA & Performance Incident Runbook",
                "chunk": "Payment gateway downtime procedures: Check transaction logs, roll back recent routing patches if error rate exceeds 5%.",
                "metadata": {"type": "sop", "category": "engineering"}
            },
            {
                "id": "doc-3",
                "title": "Q3 2026 SaaS Pricing Matrix",
                "chunk": "Enterprise Tier includes dedicated CSM and AI Copilot access. Add-on Advanced Analytics priced at $1,200/mo.",
                "metadata": {"type": "pricing", "version": "3.1"}
            }
        ]

    async def search(self, query: str, limit: int = 3) -> List[Dict[str, Any]]:
        """Semantic search through knowledge base."""
        q_lower = query.lower()
        results = []
        for doc in self.documents_index:
            # Score relevance
            relevance = 0.5
            if any(term in doc["chunk"].lower() or term in doc["title"].lower() for term in q_lower.split()):
                relevance = 0.92
            results.append({
                "document_id": doc["id"],
                "title": doc["title"],
                "content": doc["chunk"],
                "relevance_score": relevance,
                "metadata": doc["metadata"]
            })
        results.sort(key=lambda x: x["relevance_score"], reverse=True)
        return results[:limit]

knowledge_retriever = KnowledgeRetriever()
