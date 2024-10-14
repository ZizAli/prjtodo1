import csv
from datetime import datetime, timedelta


def load_tasks(filename):
    tasks = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(row)
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(filename, fieldnames=tasks[0].keys())
        writer.writeheader()
        writer.writerows(tasks)


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks):
            print(f"{idx + 1}: {task}")


def add_task(tasks):
    name = input("Enter task name: ")
    date_str = input("Enter date and time (DD-MM-YY): ")
    duration = input("Enter duration (in hours): ")
    comments = input("Enter comments: ")
    category = input("Enter category (job, social-event, daily-routine, sports): ")
    notifications = input("Enter notifications: ")

    task = {
        "Name": name,
        "Date": date_str,
        "Duration": duration,
        "Comments": comments,
        "Category": category,
        "Notifications": notifications
    }
    tasks.append(task)


def remove_task(tasks):
    display_tasks(tasks)
    index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task removed.")
    else:
        print("Invalid task number.")


def edit_task(tasks):
    display_tasks(tasks)
    index = int(input("Enter the task number to edit: ")) - 1
    if 0 <= index < len(tasks):
        name = input("Enter new task name (leave blank to keep current): ")
        date_str = input("Enter new date and time (leave blank to keep current): ")
        duration = input("Enter new duration (leave blank to keep current): ")
        comments = input("Enter new comments (leave blank to keep current): ")
        category = input("Enter new category (leave blank to keep current): ")

        if name: tasks[index]["Name"] = name
        if date_str: tasks[index]["Date"] = date_str
        if duration: tasks[index]["Duration"] = duration
        if comments: tasks[index]["Comments"] = comments
        if category: tasks[index]["Category"] = category


        print("Task updated.")
    else:
        print("Invalid task number.")


def inspect_tasks(tasks, timeframe):
    now = datetime.now()
    filtered_tasks = []

    for task in tasks:
        task_date = datetime.strptime(task["Date"], "%d-%m-%Y")
        if timeframe == "today" and task_date.date() == now.date():
            filtered_tasks.append(task)
        elif timeframe == "this week" and now <= task_date <= now + timedelta(days=7):
            filtered_tasks.append(task)
        elif timeframe == "this month" and now.month == task_date.month and now.year == task_date.year:
            filtered_tasks.append(task)

    display_tasks(filtered_tasks)


def filter_tasks_by_category(tasks):
    category = input("Enter category to filter: ")
    filtered_tasks = [task for task in tasks if task["Category"] == category]
    display_tasks(filtered_tasks)


def summarize_duration(tasks):
    category_duration = {}

    for task in tasks:
        category = task["Category"]
        duration = float(task["Duration"])
        if category in category_duration:
            category_duration[category] += duration
        else:
            category_duration[category] = duration

    for category, total_duration in category_duration.items():
        print(f"Total duration for {category}: {total_duration} hours")


def main():
    filename = 'tasks.csv'
    tasks = load_tasks(filename)

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Remove Task")
        print("4. Inspect Tasks (Today, This Week, This Month)")
        print("5. Filter Tasks by Category")
        print("6. Summarize Duration by Category")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            edit_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            timeframe = input("Enter timeframe (today, this week, this month): ")
            inspect_tasks(tasks, timeframe)
        elif choice == "5":
            filter_tasks_by_category(tasks)
        elif choice == "6":
            summarize_duration(tasks)
        elif choice == "7":
            save_tasks(tasks, filename)
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
