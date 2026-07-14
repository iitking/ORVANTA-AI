from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from backend.auth.dependencies import get_current_user
from backend.database.models import User

router = APIRouter(prefix="/dashboard", tags=["Executive Dashboard"])

@router.get("/metrics")
async def get_dashboard_metrics(user: User = Depends(get_current_user)) -> Dict[str, Any]:
    """Retrieve high-level KPIs, AI insights, and pending executive recommendations."""
    return {
        "kpis": {
            "revenue": {"value": "$2.4M", "change": "+12.4%", "trend": "positive"},
            "customers": {"value": "18,420", "change": "+8.1%", "trend": "positive"},
            "churn_rate": {"value": "4.2%", "change": "-1.3%", "trend": "positive"},
            "pipeline_value": {"value": "$6.8M", "change": "+15.2%", "trend": "positive"}
        },
        "ai_insights": [
            {
                "id": "ins-1",
                "type": "CHURN_ALERT",
                "severity": "CRITICAL",
                "title": "23 Enterprise Accounts at High Churn Risk",
                "impact": "$184K ARR at risk",
                "evidence": "Usage decreased 24%, support tickets spiked 41% post gateway update.",
                "timestamp": "10 mins ago"
            },
            {
                "id": "ins-2",
                "type": "GROWTH_OPPORTUNITY",
                "severity": "HIGH",
                "title": "Expansion Opportunity in Enterprise Tier",
                "impact": "+$210K potential ARR",
                "evidence": "Feature retention in Advanced Analytics at 94% with low price sensitivity.",
                "timestamp": "1 hour ago"
            },
            {
                "id": "ins-3",
                "type": "SUPPORT_SPIKE",
                "severity": "WARNING",
                "title": "Payment Ticket Volume Spiked 32%",
                "impact": "2,341 affected customers ($47K revenue delay)",
                "evidence": "Correlated to Payment Gateway v2.4 patch rollout.",
                "timestamp": "3 hours ago"
            },
            {
                "id": "ins-4",
                "type": "SALES_VELOCITY",
                "severity": "POSITIVE",
                "title": "Enterprise Lead Conversion Velocity Up 18%",
                "impact": "+$320K pipeline added",
                "evidence": "Google & Microsoft accounts engaged in trial expansion.",
                "timestamp": "5 hours ago"
            }
        ],
        "ai_recommendations": [
            {
                "id": "rec-1",
                "title": "Initiate Executive Churn Intervention Campaign",
                "recommended_action": "Trigger automated customer success sequence and notify Account Executives in Slack.",
                "expected_impact": "$145K ARR protected",
                "risk_level": "MEDIUM",
                "status": "pending",
                "action_type": "n8n_slack_crm"
            },
            {
                "id": "rec-2",
                "title": "Roll Back Gateway v2.4 Patch",
                "recommended_action": "Revert to v2.3 to alleviate transaction errors for 2,341 customers.",
                "expected_impact": "Resolve 43% of active payment tickets immediately",
                "risk_level": "HIGH",
                "status": "pending",
                "action_type": "devops_workflow"
            }
        ],
        "ai_business_impact": {
            "hours_saved": 2410,
            "revenue_protected": "$384,000",
            "revenue_generated": "$210,000",
            "costs_reduced": "$58,000",
            "tasks_automated": 1842,
            "decisions_accelerated": 395
        }
    }
