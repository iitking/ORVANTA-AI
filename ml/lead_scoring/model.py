from typing import Dict, Any, List

class LeadScoringModel:
    """Predictive Lead Scoring Model for B2B pipeline conversion."""

    def score_lead(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        company_size = lead_data.get("company_size", 50)
        demo_requested = lead_data.get("demo_requested", False)
        engaged_exec = lead_data.get("decision_maker_identified", False)
        product_usage_trial = lead_data.get("trial_seats", 1)

        score = 30
        factors: List[str] = []

        if company_size >= 500:
            score += 25
            factors.append("Enterprise scale organization")
        elif company_size >= 100:
            score += 15
            factors.append("Mid-market scale organization")

        if demo_requested:
            score += 20
            factors.append("Requested interactive demo")

        if engaged_exec:
            score += 15
            factors.append("Key decision maker actively engaged")

        if product_usage_trial >= 10:
            score += 15
            factors.append(f"High product engagement ({product_usage_trial} trial users active)")

        score = min(score, 99)
        tier = "HIGH_CONVERSION_INTENT" if score >= 80 else ("WARM" if score >= 60 else "COLD")

        return {
            "company": lead_data.get("company_name", "Lead"),
            "score": score,
            "tier": tier,
            "positive_factors": factors,
            "action_priority": "IMMEDIATE" if score >= 80 else "STANDARD"
        }

lead_scorer = LeadScoringModel()
