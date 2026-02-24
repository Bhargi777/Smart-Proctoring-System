from unittest.mock import MagicMock
import numpy as np
import sys
sys.modules["mediapipe.python"] = MagicMock()

from src.core.pose import HeadPoseEstimator


def test_head_pose_estimator_initialization():
    pose = HeadPoseEstimator()
    assert pose.face_mesh is not None


def test_head_pose_returns_forward_for_blank_image():
    pose = HeadPoseEstimator()
    pose.face_mesh.process.return_value = MagicMock(multi_face_landmarks=None)
    blank_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    pose_status = pose.estimate(blank_frame)
    assert pose_status == "Looking Forward"
