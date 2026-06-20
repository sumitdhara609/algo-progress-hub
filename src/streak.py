from datetime import datetime

from storage import STREAK_FILE, load_json, save_json


def load_streak():
    return load_json(
        STREAK_FILE,
        {
            "current_streak": 0,
            "last_solved_date": "2000-01-01"
        }
    )


def update_streak():
    today = datetime.today().strftime("%Y-%m-%d")
    streak_data = load_streak()

    current_streak = streak_data.get("current_streak", 0)
    last_solved_date = streak_data.get("last_solved_date", "2000-01-01")

    if last_solved_date == today:
        return current_streak

    try:
        last_date = datetime.strptime(last_solved_date, "%Y-%m-%d")
        today_date = datetime.strptime(today, "%Y-%m-%d")

        difference = (today_date - last_date).days

        if difference == 1:
            current_streak += 1
        else:
            current_streak = 1

    except ValueError:
        current_streak = 1

    save_json(
        STREAK_FILE,
        {
            "current_streak": current_streak,
            "last_solved_date": today
        }
    )

    return current_streak