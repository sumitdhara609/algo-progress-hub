from datetime import datetime
import os
import json

DATA_FILE = "data.json"
STREAK_FILE = "streak.txt"

# Ensure files exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

if not os.path.exists(STREAK_FILE):
    with open(STREAK_FILE, "w") as f:
        f.write("0,2000-01-01")


# ------------------ JSON HELPERS ------------------

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ------------------ MENU ------------------

def show_menu():
    print("\n" + "=" * 40)
    print("        🚀 ALGO PROGRESS HUB")
    print("=" * 40)
    print("1. Add Problem")
    print("2. View Problems")
    print("3. Search Problem")
    print("4. Delete Problem")
    print("5. Show Stats")
    print("6. Exit")


# ------------------ ADD ------------------

def add_problem():
    name = input("Enter problem name: ").strip()
    difficulty = input("Enter difficulty (Easy/Medium/Hard): ").strip().capitalize()
    topic = input("Enter topic: ").strip().capitalize()
    pattern = input("Enter pattern: ").strip().capitalize()
    status = input("Enter status: ").strip().capitalize()
    link = input("Enter problem link: ").strip()

    data = load_data()

    data.append({
        "name": name,
        "difficulty": difficulty,
        "topic": topic,
        "pattern": pattern,
        "status": status,
        "link": link
    })

    save_data(data)

    print("✅ Problem added successfully!")
    update_streak()


# ------------------ VIEW ------------------

def view_problems():
    data = load_data()

    if not data:
        print("No problems added yet.")
        return

    easy, medium, hard = [], [], []

    for p in data:
        item = (p["name"], p["topic"], p["pattern"], p["status"], p["link"])

        if p["difficulty"] == "Easy":
            easy.append(item)
        elif p["difficulty"] == "Medium":
            medium.append(item)
        elif p["difficulty"] == "Hard":
            hard.append(item)

    print("\n📌 DSA Progress Dashboard\n")

    def print_section(title, problems):
        print(title)
        print("-" * 50)
        for i, (name, topic, pattern, status, link) in enumerate(problems, 1):
            print(f"{i}. {name}")
            print(f"   📂 {topic} | 🧠 {pattern} | 📌 {status}")
            print(f"   🔗 {link}")

    print_section("🟢 EASY", easy)
    print_section("\n🟡 MEDIUM", medium)
    print_section("\n🔴 HARD", hard)


# ------------------ SEARCH ------------------

def search_problem():
    keyword = input("Enter problem name to search: ").lower()

    data = load_data()

    for p in data:
        if keyword in p["name"].lower():
            print(f"\nFound: {p['name']}")
            print(f"Difficulty: {p['difficulty']}")
            print(f"Topic: {p['topic']}")
            print(f"Pattern: {p['pattern']}")
            print(f"Status: {p['status']}")
            print(f"Link: {p['link']}")
            return

    print("No matching problem found.")


# ------------------ DELETE ------------------

def delete_problem():
    data = load_data()

    if not data:
        print("No problems to delete.")
        return

    for i, p in enumerate(data, 1):
        print(f"{i}. {p['name']}")

    try:
        index = int(input("\nEnter problem number to delete: "))

        if 1 <= index <= len(data):
            removed = data.pop(index - 1)
            save_data(data)
            print(f"🗑️ Deleted: {removed['name']}")
        else:
            print("Invalid number!")

    except:
        print("Invalid input!")


# ------------------ STATS ------------------

def show_stats():
    data = load_data()

    easy = medium = hard = total = 0

    for p in data:
        total += 1
        if p["difficulty"] == "Easy":
            easy += 1
        elif p["difficulty"] == "Medium":
            medium += 1
        elif p["difficulty"] == "Hard":
            hard += 1

    print("\n📊 Your Progress Stats")
    print("-" * 40)
    print(f"Total Problems Solved : {total}")
    print(f"Easy   : {easy}")
    print(f"Medium : {medium}")
    print(f"Hard   : {hard}")

    goal = 100
    progress = (total / goal) * 100 if goal else 0
    print(f"\n🎯 Progress towards {goal}: {progress:.2f}%")

    try:
        with open(STREAK_FILE, "r") as file:
            streak, _ = file.read().split(",")
            print(f"\n🔥 Current Streak: {streak} days")
    except:
        print("\n🔥 Current Streak: 0 days")


# ------------------ STREAK ------------------

def update_streak():
    today = datetime.today().strftime("%Y-%m-%d")

    try:
        with open(STREAK_FILE, "r") as file:
            streak, last_date = file.read().split(",")

        streak = int(streak)

        if last_date == today:
            return

        last_date_obj = datetime.strptime(last_date, "%Y-%m-%d")
        today_obj = datetime.strptime(today, "%Y-%m-%d")

        diff = (today_obj - last_date_obj).days

        if diff == 1:
            streak += 1
        else:
            streak = 1

    except:
        streak = 1

    with open(STREAK_FILE, "w") as file:
        file.write(f"{streak},{today}")


# ------------------ MAIN ------------------

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_problem()
        elif choice == "2":
            view_problems()
        elif choice == "3":
            search_problem()
        elif choice == "4":
            delete_problem()
        elif choice == "5":
            show_stats()
        elif choice == "6":
            print("🔥 Stay consistent. See you in the next compile! 👋")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()