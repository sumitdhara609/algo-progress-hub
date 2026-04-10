from datetime import datetime

import os

DATA_FILE = "data.txt"

if not os.path.exists(DATA_FILE):
    open(DATA_FILE, "w").close()


def show_menu():
    print("\n" + "=" * 35)
    print("         ALGO PROGRESS HUB")
    print("=" * 35)
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
    link = input("Enter problem link (or type Custom): ").strip()

    with open(DATA_FILE, "a") as file:
        file.write(f"{name},{difficulty},{topic},{link}\n")

    print("✅ Problem successfully saved!")
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
            name, difficulty, topic, link = line.strip().split(",")

            if difficulty == "Easy":
                easy.append((name, topic, link))
            elif difficulty == "Medium":
                medium.append((name, topic, link))
            elif difficulty == "Hard":
                hard.append((name, topic, link))

        print("\n📌 Your Problems:\n")

        print("🟢 EASY")
        print("-" * 40)
        for i, (name, topic, link) in enumerate(easy, 1):
            print(f"{i}. {name} ({topic})")
            print(f"   🔗 {link}")

        print("\n🟡 MEDIUM")
        print("-" * 40)
        for i, (name, topic, link) in enumerate(medium, 1):
            print(f"{i}. {name} ({topic})")
            print(f"   🔗 {link}")

        print("\n🔴 HARD")
        print("-" * 40)
        for i, (name, topic, link) in enumerate(hard, 1):
            print(f"{i}. {name} ({topic})")
            print(f"   🔗 {link}")

    except FileNotFoundError:
        print("No data found.")


def search_problem():
    keyword = input("Enter problem name to search: ").lower()

    try:
        with open(DATA_FILE, "r") as file:
            found = False

            for line in file:
                name, difficulty = line.strip().split(",")

                if keyword in name.lower():
                    print(f"Found: {name} [{difficulty}]")
                    found = True

            if not found:
                print("No matching problem found.")

    except FileNotFoundError:
        print("No data found.")


def delete_problem():
    view_problems()

    try:
        index = int(input("\nEnter problem number to delete: "))
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()

        if 1 <= index <= len(lines):
            removed = lines.pop(index - 1)

            with open(DATA_FILE, "w") as file:
                file.writelines(lines)

            name, _ = removed.strip().split(",")
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

                if len(parts) != 4:
                    continue

                _, difficulty, _, _ = parts
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

        # 🎯 Progress Goal
        goal = 100
        progress = (total / goal) * 100 if goal else 0
        print(f"\n🎯 Progress towards {goal} problems: {progress:.2f}%")

        # 🔥 Streak (correct placement)
        try:
            with open("streak.txt", "r") as file:
                streak, _ = file.read().split(",")
                print(f"\n🔥 Current Streak: {streak} days")
        except:
            print("\n🔥 Current Streak: 0 days")

    except FileNotFoundError:
        print("No data available.")

def update_streak():
    today = datetime.today().strftime("%Y-%m-%d")

    try:
        with open("streak.txt", "r") as file:
            streak, last_date = file.read().split(",")

        streak = int(streak)

        if last_date == today:
            return  # already counted today

        last_date_obj = datetime.strptime(last_date, "%Y-%m-%d")
        today_obj = datetime.strptime(today, "%Y-%m-%d")

        difference = (today_obj - last_date_obj).days

        if difference == 1:
            streak += 1
        elif difference > 1:
            streak = 1  # reset streak
        else:
            return

    except:
        streak = 1  # first time

    with open("streak.txt", "w") as file:
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
            print("🔥 Stay consistent. See you in the next compile!👋")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()