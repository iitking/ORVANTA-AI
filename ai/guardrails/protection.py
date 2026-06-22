import re
from typing import Dict, List, Optional, Tuple

class AIGuardrails:
    """Enterprise AI Guardrails for prompt injection prevention, PII masking, and role safety."""

    # Common prompt injection signatures
    INJECTION_PATTERNS = [
        r"ignore (all )?previous instructions",
        r"disregard the above",
        r"system override",
        r"you are now a new persona",
        r"reveal your internal system prompt",
        r"drop tables",
        r"delete from users",
        r"bypass safety protocols",
    ]

    # Sensitive PII patterns
    EMAIL_PATTERN = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    CREDIT_CARD_PATTERN = r"\b(?:\d{4}[-\s]?){3}\d{4}\b"
    SSN_PATTERN = r"\b\d{3}-\d{2}-\d{4}\b"
    API_KEY_PATTERN = r"\b(sk-[a-zA-Z0-9]{20,}|ghp_[a-zA-Z0-9]{20,})\b"

    # Agent capability matrix
    AGENT_PERMISSIONS: Dict[str, Dict[str, List[str]]] = {
        "sales_agent": {
            "read": ["crm", "analytics", "leads"],
            "write": ["crm_tasks", "outreach_drafts"],
            "forbidden": ["billing", "delete_customer", "admin_settings"]
        },
        "support_agent": {
            "read": ["tickets", "customer_history", "docs"],
            "write": ["ticket_notes", "suggested_responses"],
            "forbidden": ["execute_refund", "delete_data"]
        },
        "data_agent": {
            "read": ["sql_database", "metrics", "warehouse"],
            "write": ["analytics_cache"],
            "forbidden": ["drop_table", "delete", "update", "insert"]
        },
        "strategy_agent": {
            "read": ["financial_summary", "churn_reports", "market_data"],
            "write": ["growth_recommendations"],
            "forbidden": ["direct_execution"]
        }
    }

    @classmethod
    def check_prompt_injection(cls, user_prompt: str) -> Tuple[bool, Optional[str]]:
        """Detect prompt injection attempts."""
        clean_text = user_prompt.lower()
        for pattern in cls.INJECTION_PATTERNS:
            if re.search(pattern, clean_text):
                return True, f"Potential prompt injection detected matching pattern: {pattern}"
        return False, None

    @classmethod
    def mask_pii(cls, text: str) -> str:
        """Mask sensitive PII in inputs/logs."""
        text = re.sub(cls.CREDIT_CARD_PATTERN, "[REDACTED_CARD]", text)
        text = re.sub(cls.SSN_PATTERN, "[REDACTED_SSN]", text)
        text = re.sub(cls.API_KEY_PATTERN, "[REDACTED_API_KEY]", text)
        return text

    @classmethod
    def validate_agent_action(cls, agent_name: str, action_name: str) -> Tuple[bool, Optional[str]]:
        """Ensure agent cannot execute forbidden actions outside its permission boundary."""
        permissions = cls.AGENT_PERMISSIONS.get(agent_name)
        if not permissions:
            return True, None

        if action_name in permissions.get("forbidden", []):
            return False, f"Action '{action_name}' is explicitly FORBIDDEN for agent '{agent_name}'."
        return True, None
