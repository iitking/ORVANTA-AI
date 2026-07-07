import time
from typing import Dict, Any, List, Optional
from ai.guardrails.protection import AIGuardrails
from ai.llm.client import llm_client
from agents.data_agent.data_agent import DataAgent
from agents.sales_agent.sales_agent import SalesAgent
from agents.support_agent.support_agent import SupportAgent
from agents.customer_agent.customer_agent import CustomerAgent
from agents.strategy_agent.strategy_agent import StrategyAgent
from agents.automation_agent.automation_agent import AutomationAgent

class MasterOrchestrator:
    """
    Autonomous Multi-Agent LangGraph Orchestrator for ORVANTA AI.
    Executes the closed-loop cycle: Observe -> Understand -> Analyze -> Predict -> Recommend -> Approve -> Execute -> Measure.
    """

    def __init__(self):
        self.data_agent = DataAgent()
        self.sales_agent = SalesAgent()
        self.support_agent = SupportAgent()
        self.customer_agent = CustomerAgent()
        self.strategy_agent = StrategyAgent()
        self.automation_agent = AutomationAgent()

    async def run(self, user_query: str, user_role: str = "executive") -> Dict[str, Any]:
        start_time = time.time()

        # Step 1: AI Guardrails - Prompt Injection & PII Masking
        is_injection, injection_msg = AIGuardrails.check_prompt_injection(user_query)
        if is_injection:
            return {
                "success": False,
                "error": injection_msg,
                "safety_alert": "Query blocked by AI Guardrails (prompt injection attempt detected)."
            }

        sanitized_query = AIGuardrails.mask_pii(user_query)

        # Step 2: Intent Classification & Routing
        intent = self._classify_intent(sanitized_query)
        agent_contributions: List[Dict[str, Any]] = []

        # Step 3: Multi-Agent Execution based on Intent
        if intent == "CUSTOMER_CHURN":
            cust_res = await self.customer_agent.analyze(sanitized_query)
            data_res = await self.data_agent.analyze(sanitized_query)
            agent_contributions.extend([cust_res, data_res])
            primary_agent = "Customer Intelligence Agent"

        elif intent == "SALES_LEADS":
            sales_res = await self.sales_agent.analyze(sanitized_query)
            agent_contributions.append(sales_res)
            primary_agent = "Sales Intelligence Agent"

        elif intent == "SUPPORT_DIAGNOSTICS":
            supp_res = await self.support_agent.analyze(sanitized_query)
            agent_contributions.append(supp_res)
            primary_agent = "Support Intelligence Agent"

        else:
            # General Business Intelligence / Strategic Copilot
            data_res = await self.data_agent.analyze(sanitized_query)
            strat_res = await self.strategy_agent.formulate_strategy(sanitized_query, {})
            agent_contributions.extend([data_res, strat_res])
            primary_agent = "AI Business Copilot"

        # Step 4: Decision Engine & LLM Synthesis
        sys_prompt = (
            "You are ORVANTA AI, an autonomous enterprise business copilot. "
            "Deliver structured, quantified insights, evidence from data, and high-impact action recommendations."
        )
        llm_output = await llm_client.generate_response(
            system_prompt=sys_prompt,
            user_message=sanitized_query
        )

        # Step 5: Check Human-In-The-Loop Approval requirement
        requires_approval = False
        approval_action = None
        if intent in ["CUSTOMER_CHURN", "SUPPORT_DIAGNOSTICS"] or "action" in sanitized_query.lower():
            requires_approval = True
            approval_action = {
                "action_id": f"act-{int(time.time())}",
                "description": "Trigger automated customer success sequence and create CRM outreach task for high-risk accounts.",
                "risk_level": "MEDIUM",
                "target_system": "HubSpot & Slack",
                "estimated_roi": "$145K ARR protected"
            }

        latency_ms = int((time.time() - start_time) * 1000)

        return {
            "success": True,
            "query": sanitized_query,
            "intent": intent,
            "primary_agent": primary_agent,
            "answer": llm_output["text"],
            "agent_contributions": agent_contributions,
            "requires_human_approval": requires_approval,
            "pending_approval": approval_action,
            "latency_ms": latency_ms,
            "tokens": llm_output.get("token_usage", 0),
            "model_used": llm_output.get("model", "orvanta-intelligence-v1"),
        }

    def _classify_intent(self, query: str) -> str:
        q = query.lower()
        if "churn" in q or "health" in q or "customer" in q or "retention" in q:
            return "CUSTOMER_CHURN"
        elif "lead" in q or "sales" in q or "pipeline" in q or "conversion" in q:
            return "SALES_LEADS"
        elif "ticket" in q or "support" in q or "incident" in q or "issue" in q:
            return "SUPPORT_DIAGNOSTICS"
        elif "revenue" in q or "growth" in q or "pricing" in q or "strategy" in q:
            return "STRATEGY_GROWTH"
        return "GENERAL_ANALYTICS"

orchestrator = MasterOrchestrator()
