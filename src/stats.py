from collections import Counter

from goals import load_goal
from problems import load_problems
from streak import load_streak


def calculate_stats():
    problems = load_problems()

    total = len(problems)

    difficulty_count = Counter(problem.get("difficulty", "Unknown") for problem in problems)
    status_count = Counter(problem.get("status", "Unknown") for problem in problems)
    topic_count = Counter(problem.get("topic", "Unknown") for problem in problems)
    pattern_count = Counter(problem.get("pattern", "Unknown") for problem in problems)

    solved = status_count.get("Solved", 0)
    solved_percentage = (solved / total) * 100 if total else 0

    return {
        "total": total,
        "solved": solved,
        "solved_percentage": solved_percentage,
        "difficulty_count": difficulty_count,
        "status_count": status_count,
        "topic_count": topic_count,
        "pattern_count": pattern_count
    }


def show_counter(title, counter):
    print(f"\n{title}")
    print("-" * 40)

    if not counter:
        print("No data available.")
        return

    for key, value in counter.most_common():
        print(f"{key}: {value}")


def show_stats():
    stats = calculate_stats()
    streak = load_streak()
    goal = load_goal()

    print("\nProgress Analytics")
    print("=" * 50)

    print(f"Total Problems     : {stats['total']}")
    print(f"Solved Problems    : {stats['solved']}")
    print(f"Solved Progress    : {stats['solved_percentage']:.2f}%")

    print(f"\nCurrent Streak     : {streak.get('current_streak', 0)} day(s)")

    print("\nDaily Goal")
    print("-" * 40)
    print(f"Goal               : {goal.get('daily_goal', 0)} problem(s)/day")
    print(f"Completed Today    : {goal.get('today_count', 0)}")

    remaining = goal.get("daily_goal", 0) - goal.get("today_count", 0)

    if remaining <= 0:
        print("Status             : Completed")
    else:
        print(f"Remaining          : {remaining}")

    show_counter("Difficulty Breakdown", stats["difficulty_count"])
    show_counter("Status Breakdown", stats["status_count"])
    show_counter("Topic Breakdown", stats["topic_count"])
    show_counter("Pattern Breakdown", stats["pattern_count"])