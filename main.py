import os

DATA_FILE = "data.txt"

if not os.path.exists(DATA_FILE):
    open(DATA_FILE, "w").close()


def show_menu():
    print("\n" + "=" * 35)
    print("         DSA TRACKER")
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

    with open(DATA_FILE, "a") as file:
        file.write(f"{name},{difficulty}\n")

    print("✅ Problem successfully saved to tracker!")


def view_problems():
    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No problems added yet.")
            return

        print("\n📌 Your Problems:")
        print("-" * 35)

        for i, line in enumerate(lines, 1):
            name, difficulty = line.strip().split(",")
            print(f"{i}. {name} [{difficulty}]")

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
    easy = medium = hard = 0

    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                _, difficulty = line.strip().split(",")

                if difficulty == "Easy":
                    easy += 1
                elif difficulty == "Medium":
                    medium += 1
                elif difficulty == "Hard":
                    hard += 1

        print("\n📊 Your Progress Stats")
        print("-" * 35)
        print(f"Easy   : {easy}")
        print(f"Medium : {medium}")
        print(f"Hard   : {hard}")

    except FileNotFoundError:
        print("No data available.")


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
            print("🔥 Stay consistent. See you in the next compile!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()