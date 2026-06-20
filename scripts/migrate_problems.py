import json
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
PROBLEMS_FILE = BASE_DIR / "data" / "problems.json"


def generate_problem_id(name):
    return (
        name.lower()
        .strip()
        .replace(" ", "-")
        .replace("'", "")
        .replace(",", "")
    )


def load_problems():
    with open(PROBLEMS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_problems(problems):
    with open(PROBLEMS_FILE, "w", encoding="utf-8") as file:
        json.dump(problems, file, indent=4)


def migrate():
    problems = load_problems()
    used_ids = set()
    migrated_count = 0

    for problem in problems:
        name = problem.get("name", "untitled-problem")

        if "id" not in problem or not problem["id"]:
            base_id = generate_problem_id(name)
            problem_id = base_id
            counter = 2

            while problem_id in used_ids:
                problem_id = f"{base_id}-{counter}"
                counter += 1

            problem["id"] = problem_id
            migrated_count += 1

        used_ids.add(problem["id"])

        if "created_at" not in problem or not problem["created_at"]:
            problem["created_at"] = "2026-04-14"
            migrated_count += 1

    save_problems(problems)

    print("Migration completed successfully.")
    print(f"Updated fields: {migrated_count}")
    print(f"Total problems: {len(problems)}")


if __name__ == "__main__":
    migrate()