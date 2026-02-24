import cv2
import time
from src.utils.config import Config
from src.utils.logger import ProctorLogger
from src.utils.screenshot import ScreenshotCapture
from src.core.detector import FaceDetector
from src.core.pose import HeadPoseEstimator
from src.core.scorer import RiskScorer

def main():
    print("Starting Smart AI Proctoring System...")
    
    cap = cv2.VideoCapture(Config.CAMERA_INDEX)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Initialize modules
    detector = FaceDetector()
    pose_estimator = HeadPoseEstimator()
    scorer = RiskScorer()
    logger = ProctorLogger()
    screenshot = ScreenshotCapture()

    fps_delay = int(1000 / Config.TARGET_FPS)
    print(f"Systems initialized. Target FPS: {Config.TARGET_FPS}. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame. Exiting...")
            break

        # Process frame
        face_count, face_boxes = detector.detect(frame)
        pose_status = "Looking Forward"
        
        if face_count == 1:
            pose_status = pose_estimator.estimate(frame)
            
        # Draw bounding boxes
        for (x, y, w, h) in face_boxes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
        current_score, violations = scorer.process(face_count, pose_status)
        
        for v in violations:
            logger.log_violation(v, f"Score updated to {current_score}")
            screenshot.capture(frame, reason=v)

        # Overlay Info
        cv2.putText(frame, f"Faces: {face_count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, f"Pose: {pose_status}", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(frame, f"Risk Score: {current_score}", (10, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        if violations:
            cv2.putText(frame, f"WARNING: {violations[-1]}", (10, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow(Config.WINDOW_NAME, frame)

        if cv2.waitKey(fps_delay) & 0xFF == ord('q'):
            print("Exiting and saving session...")
            break

    cap.release()
    cv2.destroyAllWindows()
    logger.save_session(current_score)

if __name__ == "__main__":
    main()
