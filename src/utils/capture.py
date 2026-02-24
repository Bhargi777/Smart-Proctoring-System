import os
import cv2
from datetime import datetime
from src.core.config import SCREENSHOTS_DIR

class CaptureUtil:
    def __init__(self, session_id: str):
        self.session_dir = os.path.join(SCREENSHOTS_DIR, session_id)
        os.makedirs(self.session_dir, exist_ok=True)

    def save_screenshot(self, frame, event_name: str) -> str:
        """
        Saves a screenshot to disk and returns the file path.
        """
        timestamp = datetime.now().strftime("%H%M%S_%f")[:10]
        filename = f"{timestamp}_{event_name}.jpg"
        filepath = os.path.join(self.session_dir, filename)
        cv2.imwrite(filepath, frame)
        return filepath
