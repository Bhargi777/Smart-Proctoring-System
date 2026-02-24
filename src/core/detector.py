import cv2
import mediapipe as mp
from src.utils.config import Config

class FaceDetector:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection
        self.detector = self.mp_face_detection.FaceDetection(
            model_selection=1, # 0 for short-range, 1 for full-range
            min_detection_confidence=Config.MIN_DETECTION_CONFIDENCE
        )

    def detect(self, frame):
        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.detector.process(rgb_frame)
        
        face_count = 0
        boxes = []
        
        if results.detections:
            face_count = len(results.detections)
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                # convert relative coordinates to absolute
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                             int(bboxC.width * iw), int(bboxC.height * ih)
                boxes.append((x, y, w, h))
                
        return face_count, boxes
