def display_list(list):
    if not list:
        print("Your list is empty.")
    else:
        print("\nTList:")
        for idx, task in enumerate(list, start=1):
            print(f"{idx}. {task}")

def main():
    list = []

    while True:
        print("\nTo-Do List Menu:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_list(list)
        elif choice == '2':
            task = input("Enter the task description: ")
            list.append(task)
            print("Task added.")
        elif choice == '3':
            display_list(list)
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                if 0 <= index < len(list):
                    removed_task = list.pop(index)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
