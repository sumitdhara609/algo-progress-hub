from datetime import datetime

from storage import PROBLEMS_FILE, load_json, save_json
from streak import update_streak
from goals import update_daily_goal_progress


VALID_DIFFICULTIES = ["Easy", "Medium", "Hard"]
VALID_STATUSES = ["Solved", "Revision", "Unsolved"]


def generate_problem_id(name):
    return (
        name.lower()
        .strip()
        .replace(" ", "-")
        .replace("'", "")
        .replace(",", "")
    )


def load_problems():
    return load_json(PROBLEMS_FILE, [])


def save_problems(problems):
    save_json(PROBLEMS_FILE, problems)


def add_problem():
    name = input("Enter problem name: ").strip()

    if not name:
        print("Problem name cannot be empty.")
        return

    difficulty = input("Enter difficulty (Easy/Medium/Hard): ").strip().capitalize()

    if difficulty not in VALID_DIFFICULTIES:
        print("Invalid difficulty. Please use Easy, Medium, or Hard.")
        return

    topic = input("Enter topic: ").strip().title()
    pattern = input("Enter pattern: ").strip().title()
    status = input("Enter status (Solved/Revision/Unsolved): ").strip().capitalize()
    link = input("Enter problem link: ").strip()

    if status not in VALID_STATUSES:
        print("Invalid status. Please use Solved, Revision, or Unsolved.")
        return

    problems = load_problems()

    problem_id = generate_problem_id(name)

    for problem in problems:
        if problem.get("id") == problem_id or problem.get("name", "").lower() == name.lower():
            print("This problem already exists.")
            return

    new_problem = {
        "id": problem_id,
        "name": name,
        "difficulty": difficulty,
        "topic": topic,
        "pattern": pattern,
        "status": status,
        "link": link if link else "Custom",
        "created_at": datetime.today().strftime("%Y-%m-%d")
    }

    problems.append(new_problem)
    save_problems(problems)

    if status == "Solved":
        update_streak()
        update_daily_goal_progress()

    print("Problem added successfully!")


def view_problems():
    problems = load_problems()

    if not problems:
        print("No problems added yet.")
        return

    print("\nDSA Progress Dashboard")
    print("-" * 60)

    for index, problem in enumerate(problems, 1):
        print(f"\n{index}. {problem.get('name', 'Untitled')}")
        print(f"   Difficulty : {problem.get('difficulty', 'N/A')}")
        print(f"   Topic      : {problem.get('topic', 'N/A')}")
        print(f"   Pattern    : {problem.get('pattern', 'N/A')}")
        print(f"   Status     : {problem.get('status', 'N/A')}")
        print(f"   Link       : {problem.get('link', 'N/A')}")


def search_problem():
    keyword = input("Enter problem name/topic/pattern to search: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    problems = load_problems()

    results = [
        problem for problem in problems
        if keyword in problem.get("name", "").lower()
        or keyword in problem.get("topic", "").lower()
        or keyword in problem.get("pattern", "").lower()
    ]

    if not results:
        print("No matching problem found.")
        return

    print(f"\nFound {len(results)} matching problem(s):")
    print("-" * 60)

    for index, problem in enumerate(results, 1):
        print(f"\n{index}. {problem.get('name', 'Untitled')}")
        print(f"   Difficulty : {problem.get('difficulty', 'N/A')}")
        print(f"   Topic      : {problem.get('topic', 'N/A')}")
        print(f"   Pattern    : {problem.get('pattern', 'N/A')}")
        print(f"   Status     : {problem.get('status', 'N/A')}")
        print(f"   Link       : {problem.get('link', 'N/A')}")


def delete_problem():
    problems = load_problems()

    if not problems:
        print("No problems to delete.")
        return

    for index, problem in enumerate(problems, 1):
        print(f"{index}. {problem.get('name', 'Untitled')}")

    try:
        selected_index = int(input("\nEnter problem number to delete: ").strip())

        if selected_index < 1 or selected_index > len(problems):
            print("Invalid problem number.")
            return

        removed_problem = problems.pop(selected_index - 1)
        save_problems(problems)

        print(f"Deleted: {removed_problem.get('name', 'Untitled')}")

    except ValueError:
        print("Invalid input. Please enter a number.")