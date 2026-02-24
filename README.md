# Smart AI Proctoring System

A production-quality Smart AI Proctoring System using Python and OpenCV.

## Features
- **Real-time monitor**: Tracks user behaviors locally in real-time.
- **Face detection (MediaPipe)**: Extremely fast local inferencing.
- **No-face detection (>5s rule)**: Flags if the user disappears from view.
- **Multiple face detection**: Flags if more than one face is visible.
- **Head pose estimation**: Calculates yaw and pitch of the face to estimate view direction.
- **Violation logging**: JSON based structured logs.
- **Screenshot capture**: Local proof generation.
- **Risk scoring engine**: Accumulates a risk score based on configured penalties.

## System Architecture

The project features a highly modular structure.

```
├── src/
│   ├── core/      # ML models and business rules
│   └── utils/     # Helpers for I/O and capture
├── requirements/  # Split configurations
└── tests/         # Unit test suite
```

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

### 4. Run App
```bash
python -m src.main
```
