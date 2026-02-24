import json
import time
import os
from src.utils.config import Config

class ProctorLogger:
    def __init__(self):
        Config.setup_dirs()
        self.log_file = Config.JSON_LOG_FILE
        self.session_data = {
            "start_time": time.time(),
            "violations": [],
            "end_time": None,
            "final_risk_score": 0.0
        }
        self.violations_cache = []

    def log_violation(self, violation_type, details=""):
        time_now = time.time()
        violation = {
            "timestamp": time_now,
            "type": violation_type,
            "details": details
        }
        self.violations_cache.append(violation)
        print(f"[VIOLATION LOGGED] {violation_type} at {time_now}")

    def save_session(self, final_risk_score):
        self.session_data["end_time"] = time.time()
        self.session_data["violations"] = self.violations_cache
        self.session_data["final_risk_score"] = final_risk_score
        
        with open(self.log_file, 'w') as f:
            json.dump(self.session_data, f, indent=4)
        print(f"Session saved to {self.log_file}")
