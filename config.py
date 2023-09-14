import sys
from os import path

from reis_app_fw.utils import parse_properties

SCRIPT_DIR: str = ""
PROPERTIES: dict = {}


def get_script_dir() -> str:
    if getattr(sys, "frozen", False):
        # The script is running inside a PyInstaller bundle
        print("Running inside a PyInstaller bundle")
        return path.dirname(sys.executable)
    else:
        # The script is running in a normal Python environment
        print("Running from .py file")
        script_path = path.abspath(__file__)
        return path.dirname(script_path)


def init():
    global SCRIPT_DIR
    global PROPERTIES
    SCRIPT_DIR = get_script_dir()
    PROPERTIES = parse_properties(path.join(SCRIPT_DIR, "config.properties"))
