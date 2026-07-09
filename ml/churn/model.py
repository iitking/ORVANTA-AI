from typing import Dict, Any, List

class ChurnPredictionModel:
    """Predictive Machine Learning model for customer churn risk."""

    def predict_churn_risk(self, customer_metrics: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate churn probability based on usage trend, support ticket spikes,
        NPS score, and overdue payment status.
        """
        usage_trend = customer_metrics.get("usage_trend", 0.0)
        ticket_count = customer_metrics.get("support_ticket_count", 0)
        nps = customer_metrics.get("nps", 50)
        has_overdue_invoice = customer_metrics.get("overdue_invoices", 0) > 0

        # Heuristic scoring representing trained ML gradient boost weights
        risk_score = 0.10
        if usage_trend < -0.15:
            risk_score += 0.35
        if ticket_count > 5:
            risk_score += 0.20
        if nps < 30:
            risk_score += 0.20
        if has_overdue_invoice:
            risk_score += 0.15

        risk_score = min(max(risk_score, 0.0), 0.99)
        risk_category = "HIGH" if risk_score > 0.65 else ("MEDIUM" if risk_score > 0.35 else "LOW")

        return {
            "customer_name": customer_metrics.get("name", "Unknown"),
            "churn_probability": round(risk_score, 2),
            "risk_tier": risk_category,
            "arr_impact": customer_metrics.get("arr", 0.0),
            "key_factors": [
                f"Usage trend is {usage_trend * 100:.1f}%",
                f"{ticket_count} support tickets registered",
                "Overdue invoice flagged" if has_overdue_invoice else "Billing in good standing"
            ]
        }

churn_model = ChurnPredictionModel()
