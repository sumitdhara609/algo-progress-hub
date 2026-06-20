from storage import ensure_data_files
from problems import add_problem, view_problems, search_problem, delete_problem
from stats import show_stats
from goals import set_daily_goal


def show_menu():
    print("\n" + "=" * 45)
    print("          ALGO PROGRESS HUB")
    print("=" * 45)
    print("1. Add Problem")
    print("2. View Problems")
    print("3. Search Problem")
    print("4. Delete Problem")
    print("5. Show Stats")
    print("6. Set Daily Goal")
    print("7. Exit")


def main():
    ensure_data_files()

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
            set_daily_goal()
        elif choice == "7":
            print("Stay consistent. See you in the next compile!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()