# Smart AI Proctoring System

A production-quality Smart AI Proctoring System using Python and OpenCV.

## Features
- Real-time webcam monitoring
- Face detection (MediaPipe)
- No-face detection (>5s rule)
- Multiple face detection
- Head pose estimation
- Violation logging with timestamps
- Screenshot capture
- Risk scoring engine

## Environment Setup

This project uses a Python virtual environment (`venv`) to isolate dependencies.

### 1. Create Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

### 3. Install Dependencies
```bash
# Runtime dependencies
pip install -r requirements/base.txt

# Development dependencies (optional)
pip install -r requirements/dev.txt

# Advanced AI features (optional)
pip install -r requirements/optional.txt
```
