from datetime import datetime
import os

DATA_FILE = "data.txt"
STREAK_FILE = "streak.txt"

if not os.path.exists(DATA_FILE):
    open(DATA_FILE, "w").close()

if not os.path.exists(STREAK_FILE):
    with open(STREAK_FILE, "w") as f:
        f.write("0,2000-01-01")


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


def add_problem():
    name = input("Enter problem name: ").strip()
    difficulty = input("Enter difficulty (Easy/Medium/Hard): ").strip().capitalize()
    topic = input("Enter topic (Array/String/etc): ").strip().capitalize()
    pattern = input("Enter pattern (Hashing/DP/etc): ").strip().capitalize()
    status = input("Enter status (Solved/Revision/Unsolved): ").strip().capitalize()
    link = input("Enter problem link: ").strip()

    with open(DATA_FILE, "a") as file:
        file.write(f"{name},{difficulty},{topic},{pattern},{status},{link}\n")

    print("✅ Problem added successfully!")
    update_streak()


def view_problems():
    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No problems added yet.")
            return

        easy, medium, hard = [], [], []

        for line in lines:
            parts = line.strip().split(",")

            if len(parts) < 6:
                continue

            name, difficulty, topic, pattern, status, link = parts
            data = (name, topic, pattern, status, link)

            if difficulty == "Easy":
                easy.append(data)
            elif difficulty == "Medium":
                medium.append(data)
            elif difficulty == "Hard":
                hard.append(data)

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

    except FileNotFoundError:
        print("No data found.")


def search_problem():
    keyword = input("Enter problem name to search: ").lower()

    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) < 6:
                    continue

                name, difficulty, topic, pattern, status, link = parts

                if keyword in name.lower():
                    print(f"\nFound: {name}")
                    print(f"Difficulty: {difficulty}")
                    print(f"Topic: {topic}")
                    print(f"Pattern: {pattern}")
                    print(f"Status: {status}")
                    print(f"Link: {link}")
                    return

        print("No matching problem found.")

    except FileNotFoundError:
        print("No data found.")


def delete_problem():
    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No problems to delete.")
            return

        for i, line in enumerate(lines, 1):
            parts = line.strip().split(",")
            if len(parts) >= 1:
                print(f"{i}. {parts[0]}")

        index = int(input("\nEnter problem number to delete: "))

        if 1 <= index <= len(lines):
            removed = lines.pop(index - 1)

            with open(DATA_FILE, "w") as file:
                file.writelines(lines)

            name = removed.strip().split(",")[0]
            print(f"🗑️ Deleted: {name}")
        else:
            print("Invalid number!")

    except:
        print("Error deleting problem.")


def show_stats():
    easy = medium = hard = total = 0

    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) < 6:
                    continue

                _, difficulty, _, _, _, _ = parts
                total += 1

                if difficulty == "Easy":
                    easy += 1
                elif difficulty == "Medium":
                    medium += 1
                elif difficulty == "Hard":
                    hard += 1

        print("\n📊 Your Progress Stats")
        print("-" * 40)
        print(f"Total Problems Solved : {total}")
        print(f"Easy   : {easy}")
        print(f"Medium : {medium}")
        print(f"Hard   : {hard}")

        goal = 100
        progress = (total / goal) * 100 if goal else 0
        print(f"\n🎯 Progress towards {goal} problems: {progress:.2f}%")

        try:
            with open(STREAK_FILE, "r") as file:
                streak, _ = file.read().split(",")
                print(f"\n🔥 Current Streak: {streak} days")
        except:
            print("\n🔥 Current Streak: 0 days")

    except FileNotFoundError:
        print("No data available.")


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
        elif diff > 1:
            streak = 1

    except:
        streak = 1

    with open(STREAK_FILE, "w") as file:
        file.write(f"{streak},{today}")


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