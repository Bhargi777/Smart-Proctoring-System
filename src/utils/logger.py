import json
import time
import os
from typing import Dict, Any, List
from src.utils.config import Config

class ProctorLogger:
    def __init__(self) -> None:
        Config.setup_dirs()
        self.log_file: str = Config.JSON_LOG_FILE
        self.session_data: Dict[str, Any] = {
            "start_time": time.time(),
            "violations": [],
            "end_time": None,
            "final_risk_score": 0.0
        }
        self.violations_cache: List[Dict[str, Any]] = []

    def log_violation(self, violation_type: str, details: str = "") -> None:
        time_now = time.time()
        violation = {
            "timestamp": time_now,
            "type": violation_type,
            "details": details
        }
        self.violations_cache.append(violation)
        print(f"[VIOLATION LOGGED] {violation_type} at {time_now}")

    def save_session(self, final_risk_score: float) -> None:
        self.session_data["end_time"] = time.time()
        self.session_data["violations"] = self.violations_cache
        self.session_data["final_risk_score"] = float(final_risk_score)
        
        with open(self.log_file, 'w') as f:
            json.dump(self.session_data, f, indent=4)
        print(f"Session saved to {self.log_file}")
