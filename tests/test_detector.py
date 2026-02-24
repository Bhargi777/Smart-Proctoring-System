from unittest.mock import MagicMock
import numpy as np
import sys

# Mock mediapipe before importing the module that relies on it
sys.modules["mediapipe.python"] = MagicMock()

from src.core.detector import FaceDetector


def test_face_detector_initialization():
    detector = FaceDetector()
    assert detector.detector is not None


def test_detect_no_face_in_blank_image():
    detector = FaceDetector()
    detector.detector.process.return_value = MagicMock(detections=None)
    blank_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    face_count, boxes = detector.detect(blank_frame)
    assert face_count == 0
    assert len(boxes) == 0
