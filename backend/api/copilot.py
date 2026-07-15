from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Dict, Any, Optional
from backend.auth.dependencies import get_current_user
from backend.database.models import User
from agents.orchestrator.langgraph_workflow import orchestrator

router = APIRouter(prefix="/copilot", tags=["AI Business Copilot"])

class CopilotQueryRequest(BaseModel):
    message: str
    context_filters: Optional[Dict[str, Any]] = None

@router.post("/query")
async def copilot_query(
    req: CopilotQueryRequest,
    user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """Execute query across multi-agent LangGraph orchestrator."""
    result = await orchestrator.run(
        user_query=req.message,
        user_role=user.role
    )
    return result
