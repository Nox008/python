""" tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    match choice:
        case '1':  # View tasks
            if not tasks:
                print("No tasks added yet.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks):
                    status = "✅ Done" if task['done'] else "❌ Not Done"
                    print(f"{i + 1}. {task['title']} - {status}")

        case '2':  # Add task
            title = input("Enter task name: ")
            tasks.append({'title': title, 'done': False})
            print(f"Task '{title}' added.")

        case '3':  # Mark task as done
            if not tasks:
                print("No tasks to mark as done.")
            else:
                for i, task in enumerate(tasks):
                    status = "✅" if task['done'] else "❌"
                    print(f"{i + 1}. {task['title']} - {status}")
                try:
                    num = int(input("Enter task number to mark as done: "))
                    if 1 <= num <= len(tasks):
                        tasks[num - 1]['done'] = True
                        print(f"Marked '{tasks[num - 1]['title']}' as done.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        case '4':  # Delete task
            if not tasks:
                print("No tasks to delete.")
            else:
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task['title']}")
                try:
                    num = int(input("Enter task number to delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"Deleted '{removed['title']}'")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        case '5':  # Exit
            print("Goodbye! ✅")
            break

        case _:  # Default
            print("Invalid choice. Please enter 1-5.")
 """                        #AI code for reference ^