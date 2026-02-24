import os

class Config:
    # Camera Settings
    CAMERA_INDEX = 0
    TARGET_FPS = 15
    WINDOW_NAME = "Smart AI Proctoring System"
    
    # Face Detection
    MIN_DETECTION_CONFIDENCE = 0.5
    MIN_TRACKING_CONFIDENCE = 0.5
    
    # Pose Estimation Thresholds
    POSE_YAW_THRESHOLD = 10
    POSE_PITCH_THRESHOLD = 10
    
    # Proctoring Rules
    NO_FACE_TIMEOUT_SEC = 5.0
    
    # Output Directories
    OUTPUT_DIR = "logs"
    SCREENSHOT_DIR = os.path.join(OUTPUT_DIR, "screenshots")
    JSON_LOG_FILE = os.path.join(OUTPUT_DIR, "session_log.json")

    @classmethod
    def setup_dirs(cls):
        os.makedirs(cls.SCREENSHOT_DIR, exist_ok=True)
