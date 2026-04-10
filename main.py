def show_menu():
    print("\n" + "="*30)
    print("       DSA TRACKER")
    print("="*30)
    print("1. Add Problem")
    print("2. View Problems")
    print("3. Show Stats")
    print("4. Exit")

def add_problem():
    name = input("Enter problem name: ").strip()
    difficulty = input("Enter difficulty (Easy/Medium/Hard): ").strip().capitalize()

    if difficulty not in ["Easy", "Medium", "Hard"]:
        print("Invalid difficulty!")
        return

    with open("data.txt", "a") as file:
        file.write(f"{name},{difficulty}\n")

    print("Problem added successfully!")
def view_problems():
    try:
        with open("data.txt", "r") as file:
            lines = file.readlines()

            if not lines:
                print("No problems added yet.")
                return

            print("\nYour Problems:")
            print("-"*30)

            for i, line in enumerate(lines, 1):
                name, difficulty = line.strip().split(",")
                print(f"{i}. {name} [{difficulty}]")

    except FileNotFoundError:
        print("No data found.")
def show_stats():
    easy = 0
    medium = 0
    hard = 0

    try:
        with open("data.txt", "r") as file:
            for line in file:
                _, difficulty = line.strip().split(",")

                if difficulty == "Easy":
                    easy += 1
                elif difficulty == "Medium":
                    medium += 1
                elif difficulty == "Hard":
                    hard += 1

        print("\nYour Progress:")
        print("-"*30)
        print(f"Easy   : {easy}")
        print(f"Medium : {medium}")
        print(f"Hard   : {hard}")

    except FileNotFoundError:
        print("No data available.")
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_problem()
        elif choice == "2":
            view_problems()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            print("Exiting... Keep coding")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()