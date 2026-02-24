import json
import os
from src.utils.config import Config


def print_report():
    log_file = Config.JSON_LOG_FILE
    if not os.path.exists(log_file):
        print(f"No log file found at {log_file}")
        return

    with open(log_file, "r") as f:
        data = json.load(f)

    print("=== Smart AI Proctoring Session Report ===")
    print(f"Start Time: {data.get('start_time')}")
    print(f"End Time: {data.get('end_time')}")
    print(f"Final Risk Score: {data.get('final_risk_score', 0)}")

    violations = data.get("violations", [])
    print(f"\nTotal Violations Recorded: {len(violations)}")

    for i, v in enumerate(violations, 1):
        print(f"  {i}. [Time: {v['timestamp']:.2f}] {v['type']} - {v['details']}")

    print("\nReport Complete.")


if __name__ == "__main__":
    print_report()
