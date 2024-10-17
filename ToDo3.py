import csv

print("My To Do List")

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
TIME_FRAMES = ["today", "this week", "this month"]


def get_tasks_from_input():
    my_task = input(
        "Add tasks (format: description, severity (duration), deadline (Weekday), time frame (today, this week, this month), category, notification, status): \n")
    tasks = my_task.split(';')
    valid_tasks = []
    for todo, text in enumerate(tasks, start=1):
        task = text.split(',')
        if len(task) == 7:
            description = task[0].strip()
            severity = task[1].strip()
            deadline = task[2].strip()
            time_frame = task[3].strip().lower()
            if deadline not in WEEKDAYS:
                deadline = "Invalid Day"
            if time_frame not in TIME_FRAMES:
                time_frame = "Invalid Time Frame"
            category = task[4].strip()
            notification = task[5].strip()
            status = task[6].strip()
            valid_tasks.append((description, severity, deadline, time_frame, category, notification, status))
            print(f"{todo}. [Description: {description}] [Severity (Duration): {severity}] [Deadline: {deadline}] "
                  f"[Time Frame: {time_frame}] [Category: {category}] [Notification: {notification}] [Status: {status}]")
        else:
            print(f"{todo}. Invalid entry format: {text.strip()}")
    return valid_tasks


def write_tasks_to_csv(tasks, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['Description', 'Severity', 'Deadline (Weekday)', 'Time Frame', 'Category', 'Notification', 'Status'])
        writer.writerows(tasks)


def filter_tasks(tasks, time_frame, category=None):
    filtered_tasks = []
    for task in tasks:
        deadline_weekday = task[2].strip()
        task_time_frame = task[3].strip()

        if category and task[4].strip().lower() != category.lower():
            continue

        if time_frame == task_time_frame and time_frame in TIME_FRAMES:
            filtered_tasks.append(task)

    return filtered_tasks


def summarize_duration(tasks, time_frame, category=None):
    duration_summary = {}

    for task in tasks:
        task_time_frame = task[3].strip()

        severity = task[1].strip()
        task_category = task[4].strip()
        if category and task_category.lower() != category.lower():
            continue

        if time_frame == task_time_frame:
            duration_summary[task_category] = duration_summary.get(task_category, 0) + int(severity)

    return duration_summary


def main():
    print("My ToDo List Project")
    tasks = get_tasks_from_input()

    if tasks:
        csv_file_name = 'Mytask.csv'
        write_tasks_to_csv(tasks, csv_file_name)
        print(f"Tasks have been written to {csv_file_name}.")

        time_frame = input("Which time frame would you like to inspect? (today/this week/this month): ").strip().lower()
        category = input("Enter category to filter by (or press Enter to skip): ").strip()

        filtered_tasks = filter_tasks(tasks, time_frame, category if category else None)

        if filtered_tasks:
            print(f"Tasks for {time_frame}{' in category: ' + category if category else ''}:")
            for task in filtered_tasks:
                print(f"[Description: {task[0]}] [Severity (Duration): {task[1]}] [Deadline: {task[2]}] "
                      f"[Time Frame: {task[3]}] [Category: {task[4]}] [Notification: {task[5]}] [Status: {task[6]}]")
        else:
            print(f"No tasks found for {time_frame}{' in category: ' + category if category else ''}.")

        summary = summarize_duration(tasks, time_frame, category if category else None)
        if summary:
            print("Duration Summary:")
            for cat, total_duration in summary.items():
                print(f"Category: {cat}, Total Duration: {total_duration}")
        else:
            print("No duration summary available for the selected criteria.")
    else:
        print("No valid tasks to write.")


if __name__ == "__main__":
    main()
