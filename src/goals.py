from datetime import datetime

from storage import GOAL_FILE, load_json, save_json


def load_goal():
    return load_json(
        GOAL_FILE,
        {
            "daily_goal": 3,
            "last_updated": "",
            "today_count": 0
        }
    )


def save_goal(goal):
    save_json(GOAL_FILE, goal)


def update_daily_goal_progress():
    goal = load_goal()
    today = datetime.today().strftime("%Y-%m-%d")

    if goal.get("last_updated") != today:
        goal["today_count"] = 0
        goal["last_updated"] = today

    goal["today_count"] += 1
    save_goal(goal)


def set_daily_goal():
    goal = load_goal()

    try:
        new_goal = int(input("Enter daily problem goal: ").strip())

        if new_goal <= 0:
            print("Goal must be greater than 0.")
            return

        goal["daily_goal"] = new_goal
        save_goal(goal)

        print("Daily goal updated successfully!")

    except ValueError:
        print("Invalid input. Please enter a number.")