from src.utils.config import Config
import os


def test_config_paths():
    assert Config.OUTPUT_DIR == "logs"
    assert Config.SCREENSHOT_DIR == os.path.join("logs", "screenshots")


def test_config_fps():
    assert Config.TARGET_FPS == 15
