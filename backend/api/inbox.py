from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List
from backend.auth.dependencies import get_current_user, require_permission
from backend.auth.rbac import Permission
from backend.database.models import User
from agents.automation_agent.automation_agent import AutomationAgent

router = APIRouter(prefix="/inbox", tags=["AI Inbox & Human-in-the-Loop"])

automation_agent = AutomationAgent()

# In-memory store for interactive demo / development state
APPROVAL_ITEMS = [
    {
        "id": "act-101",
        "priority": "HIGH",
        "title": "Customer ABC Corp Churn Intervention",
        "summary": "Customer ABC Corp shows 78% churn probability with $340K ARR at risk.",
        "recommended_action": "Schedule executive call & trigger customer success retention package.",
        "target_systems": ["HubSpot CRM", "Slack #exec-churn", "Gmail"],
        "status": "pending",
        "estimated_roi": "$340,000 protected"
    },
    {
        "id": "act-102",
        "priority": "GROWTH",
        "title": "Launch Enterprise Expansion Campaign for Tech Sector",
        "summary": "Enterprise conversion improved 21%. Potential additional ARR: $280K.",
        "recommended_action": "Dispatch automated Apollo/HubSpot sequence for 45 qualified accounts.",
        "target_systems": ["HubSpot CRM", "n8n Workflow"],
        "status": "pending",
        "estimated_roi": "$280,000 potential ARR"
    }
]

class ActionDecisionRequest(BaseModel):
    action_id: str
    decision: str  # "approve" or "dismiss"
    notes: str = ""

@router.get("/items")
async def list_inbox_items(user: User = Depends(get_current_user)) -> List[Dict[str, Any]]:
    return APPROVAL_ITEMS

@router.post("/decide")
async def decide_action(
    req: ActionDecisionRequest,
    user: User = Depends(require_permission(Permission.APPROVE_ACTIONS))
) -> Dict[str, Any]:
    target_item = next((item for item in APPROVAL_ITEMS if item["id"] == req.action_id), None)
    if not target_item:
        raise HTTPException(status_code=404, detail="Action item not found")

    if req.decision == "approve":
        target_item["status"] = "approved"
        # Trigger automation engine via n8n
        dispatch_result = await automation_agent.trigger_workflow(
            workflow_name=req.action_id,
            payload={"action": target_item, "approved_by": user.email, "notes": req.notes}
        )
        return {
            "success": True,
            "message": f"Action {req.action_id} approved and executed successfully.",
            "execution": dispatch_result
        }
    else:
        target_item["status"] = "dismissed"
        return {"success": True, "message": f"Action {req.action_id} dismissed."}
