import cv2
import time
import argparse
from src.utils.config import Config
from src.utils.logger import ProctorLogger
from src.utils.screenshot import ScreenshotCapture
from src.core.detector import FaceDetector
from src.core.pose import HeadPoseEstimator
from src.core.scorer import RiskScorer

def parse_args():
    parser = argparse.ArgumentParser(description="Smart AI Proctoring System")
    parser.add_argument("--camera", type=int, default=Config.CAMERA_INDEX, help="Camera index")
    parser.add_argument("--debug", action="store_true", help="Enable debug logs")
    return parser.parse_args()

def main():
    args = parse_args()
    print("Starting Smart AI Proctoring System...")
    
    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        print(f"Error: Could not open webcam ({args.camera}).")
        return

    # Initialize modules
    detector = FaceDetector()
    pose_estimator = HeadPoseEstimator()
    scorer = RiskScorer()
    logger = ProctorLogger()
    screenshot = ScreenshotCapture()

    fps_delay = int(1000 / Config.TARGET_FPS)
    print(f"Systems initialized. Target FPS: {Config.TARGET_FPS}. Press 'q' to exit.")

    try:
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
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        logger.save_session(scorer.score)

if __name__ == "__main__":
    main()
