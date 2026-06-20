import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

PROBLEMS_FILE = DATA_DIR / "problems.json"
GOAL_FILE = DATA_DIR / "goal.json"
STREAK_FILE = DATA_DIR / "streak.json"


def ensure_data_files():
    DATA_DIR.mkdir(exist_ok=True)

    if not PROBLEMS_FILE.exists():
        save_json(PROBLEMS_FILE, [])

    if not GOAL_FILE.exists():
        save_json(
            GOAL_FILE,
            {
                "daily_goal": 3,
                "last_updated": "",
                "today_count": 0
            }
        )

    if not STREAK_FILE.exists():
        save_json(
            STREAK_FILE,
            {
                "current_streak": 0,
                "last_solved_date": "2000-01-01"
            }
        )


def load_json(file_path, default_value):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return default_value


def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)