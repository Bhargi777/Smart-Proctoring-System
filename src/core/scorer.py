import time
from src.utils.config import Config


class RiskScorer:
    def __init__(self):
        self.score = 0
        self.last_face_time = time.time()

    def process(self, face_count, pose_status):
        current_time = time.time()
        violations = []

        # 1. No Face Detection
        if face_count == 0:
            if (current_time - self.last_face_time) > Config.NO_FACE_TIMEOUT_SEC:
                self.score += 5
                violations.append("NO_FACE_DETECTED")
        else:
            self.last_face_time = current_time

        # 2. Multiple Faces Detection
        if face_count > 1:
            self.score += 10
            violations.append("MULTIPLE_FACES_DETECTED")

        # 3. Head Pose Anomalies
        if pose_status != "Looking Forward":
            self.score += 2
            violations.append(
                f"UNUSUAL_HEAD_POSE_{pose_status.replace(' ', '_').upper()}"
            )

        return self.score, violations
