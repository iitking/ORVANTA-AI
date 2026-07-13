from typing import Dict, Any, List

class AnomalyDetector:
    """Anomaly detection on revenue, tickets, and usage signals."""

    def detect_anomalies(self, time_series_points: List[float], metric_name: str) -> Dict[str, Any]:
        if len(time_series_points) < 3:
            return {"metric": metric_name, "anomaly_detected": False}

        avg = sum(time_series_points) / len(time_series_points)
        latest = time_series_points[-1]
        deviation = ((latest - avg) / (avg if avg != 0 else 1.0)) * 100.0

        is_anomaly = abs(deviation) > 25.0

        return {
            "metric": metric_name,
            "anomaly_detected": is_anomaly,
            "average_value": round(avg, 2),
            "latest_value": round(latest, 2),
            "deviation_percentage": round(deviation, 2),
            "severity": "CRITICAL" if abs(deviation) > 40 else ("WARNING" if is_anomaly else "NORMAL")
        }

anomaly_detector = AnomalyDetector()
