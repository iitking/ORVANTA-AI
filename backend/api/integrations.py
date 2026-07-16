from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from backend.auth.dependencies import get_current_user
from backend.database.models import User

router = APIRouter(prefix="/integrations", tags=["Integration Hub"])

AVAILABLE_INTEGRATIONS = [
    {
        "id": "hubspot",
        "name": "HubSpot CRM",
        "category": "CRM",
        "status": "connected",
        "last_sync": "4 mins ago",
        "sync_health": "99.8%",
        "records_ingested": 14200
    },
    {
        "id": "salesforce",
        "name": "Salesforce",
        "category": "CRM",
        "status": "available",
        "last_sync": None,
        "sync_health": "N/A",
        "records_ingested": 0
    },
    {
        "id": "slack",
        "name": "Slack Workspaces",
        "category": "Communication",
        "status": "connected",
        "last_sync": "Realtime",
        "sync_health": "100%",
        "records_ingested": 45100
    },
    {
        "id": "gmail",
        "name": "Google Workspace / Gmail",
        "category": "Communication",
        "status": "connected",
        "last_sync": "12 mins ago",
        "sync_health": "99.4%",
        "records_ingested": 8900
    },
    {
        "id": "postgres",
        "name": "PostgreSQL Warehouse",
        "category": "Database",
        "status": "connected",
        "last_sync": "Continuous",
        "sync_health": "100%",
        "records_ingested": 184500
    },
    {
        "id": "n8n",
        "name": "n8n Workflow Engine",
        "category": "Automation",
        "status": "connected",
        "last_sync": "Realtime Webhooks",
        "sync_health": "100%",
        "records_ingested": 2400
    },
    {
        "id": "qdrant",
        "name": "Qdrant Vector DB",
        "category": "AI / RAG",
        "status": "connected",
        "last_sync": "Continuous",
        "sync_health": "100%",
        "records_ingested": 3210
    }
]

@router.get("/list")
async def list_integrations(user: User = Depends(get_current_user)) -> List[Dict[str, Any]]:
    return AVAILABLE_INTEGRATIONS
