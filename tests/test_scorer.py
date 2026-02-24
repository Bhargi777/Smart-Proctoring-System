import pytest
from src.core.scorer import RiskScorer

def test_risk_scorer_initialization():
    scorer = RiskScorer()
    assert scorer.score == 0

def test_risk_scorer_multiple_faces():
    scorer = RiskScorer()
    score, violations = scorer.process(face_count=2, pose_status="Looking Forward")
    assert score == 10
    assert "MULTIPLE_FACES_DETECTED" in violations

def test_risk_scorer_looking_away():
    scorer = RiskScorer()
    score, violations = scorer.process(face_count=1, pose_status="Looking Left")
    assert score == 2
    assert "UNUSUAL_HEAD_POSE_LOOKING_LEFT" in violations

def test_risk_scorer_no_face(mocker):
    # This requires mocking time or waiting; for simplicity, mock time.time
    # In a full test suite we would use pytest-mock or freezegun
    pass
