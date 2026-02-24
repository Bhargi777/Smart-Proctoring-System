import cv2
import time
import os
from src.utils.config import Config


class ScreenshotCapture:
    def __init__(self):
        Config.setup_dirs()
        self.save_dir = Config.SCREENSHOT_DIR
        self.last_capture_time = 0
        self.capture_cooldown = 2.0  # limit capture to strictly every 2 seconds max

    def capture(self, frame, reason="violation"):
        now = time.time()
        if now - self.last_capture_time > self.capture_cooldown:
            filename = os.path.join(
                self.save_dir, f"screenshot_{reason}_{int(now)}.jpg"
            )
            cv2.imwrite(filename, frame)
            self.last_capture_time = now
            return filename
        return None
