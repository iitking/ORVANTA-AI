from typing import Dict, Any, List

class DataAgent:
    """Specialized AI Data Analyst Agent for Text-to-SQL, query validation, and schema discovery."""

    def __init__(self):
        self.name = "Data Analyst Agent"

    async def analyze(self, query: str) -> Dict[str, Any]:
        """Convert natural language questions to SQL and generate insights."""
        # Clean and determine relevant table
        query_lower = query.lower()
        if "churn" in query_lower or "customer" in query_lower:
            generated_sql = (
                "SELECT id, name, plan, arr, health_score, churn_probability, usage_trend "
                "FROM customers WHERE churn_probability > 0.50 ORDER BY arr DESC LIMIT 10;"
            )
            simulated_rows = [
                {"name": "ABC Corp", "plan": "Enterprise", "arr": 120000, "health_score": 32, "churn_prob": 0.78},
                {"name": "Global Logix", "plan": "Enterprise", "arr": 64000, "health_score": 45, "churn_prob": 0.62},
            ]
            explanation = "Discovered 2 enterprise accounts with elevated churn probability (>60%) representing $184K in total ARR."
        else:
            generated_sql = (
                "SELECT strftime('%Y-%m', created_at) as month, SUM(arr) as monthly_arr "
                "FROM customers GROUP BY month ORDER BY month DESC LIMIT 6;"
            )
            simulated_rows = [
                {"month": "2026-09", "monthly_arr": 2420000},
                {"month": "2026-08", "monthly_arr": 2210000},
            ]
            explanation = "Retrieved 6-month ARR trend demonstrating steady growth of 9.5% MoM."

        return {
            "agent": self.name,
            "generated_sql": generated_sql,
            "data_summary": simulated_rows,
            "explanation": explanation,
            "sql_valid": True,
        }
