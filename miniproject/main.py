from todomanager import TodoManager


def menu():
    print("\n====== TODO APP ======")
    print("1. Add Todo")
    print("2. View Todos")
    print("3. Update Todo")
    print("4. Delete Todo")
    print("5. Exit")


def main():
    manager = TodoManager()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            new_title = input("New title (leave blank to skip): ")
            status = input("Mark as completed? (yes/no/skip): ")

            completed = None
            if status.lower() == "yes":
                completed = True
            elif status.lower() == "no":
                completed = False

            manager.update_task(task_id, new_title or None, completed)

        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)

        elif choice == "5":
            print("GoodTime")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
