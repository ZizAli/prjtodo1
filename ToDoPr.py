import csv
from enum import Enum
import os


class Weekday(Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"


class TimeFrame(Enum):
    TODAY = "today"
    THIS_WEEK = "this week"
    THIS_MONTH = "this month"


class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in progress"
    DONE = "done"


class Severity(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class TaskCategory(Enum):
    WORK = "work"
    PERSONAL = "personal"
    SOCIAL = "social"
    OTHER = "other"


class Task:
    def __init__(self, description, severity, deadline: Weekday, time_frame: TimeFrame, category: TaskCategory,
                 status: TaskStatus):
        self.description = description
        self.severity = severity
        self.deadline = deadline
        self.time_frame = time_frame
        self.category = category
        self.status = status

    def __repr__(self):
        return (f"[Description: {self.description}] [Severity: {self.severity.value}] "
                f"[Deadline: {self.deadline.value}] [Time Frame: {self.time_frame.value}] "
                f"[Category: {self.category.value}] [Status: {self.status.value}]")


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def filter_tasks(self, time_frame: TimeFrame, category: TaskCategory = None):
        return [
            task for task in self.tasks
            if task.time_frame == time_frame and (not category or task.category == category)
        ]

    def summarize_status(self):
        status_summary = {
            TaskStatus.PENDING.value: 0,
            TaskStatus.IN_PROGRESS.value: 0,
            TaskStatus.DONE.value: 0,
        }
        for task in self.tasks:
            status_summary[task.status.value] += 1
        return status_summary


class TaskIO:
    def get_valid_enum_input(self, prompt, enum_class):
        valid_options = [e.value for e in enum_class]
        while True:
            user_input = input(prompt).strip().lower()
            if user_input in valid_options:
                return enum_class(next(e for e in enum_class if e.value == user_input))
            print(f"Invalid input! Please choose from: {', '.join(valid_options)}.")

    def get_task_from_input(self):
        description = input("Please add task description: ").strip()
        severity = self.get_valid_enum_input("Please add severity (high/medium/low): ", Severity)
        deadline = self.get_valid_enum_input("Please add the deadline (weekday): ", Weekday)
        time_frame = self.get_valid_enum_input("Please add the time frame (today/this week/this month): ", TimeFrame)
        category = self.get_valid_enum_input("Please add the category (work/personal/social/other): ", TaskCategory)
        status = self.get_valid_enum_input("Please add the task status (pending/in progress/done): ", TaskStatus)

        return Task(description, severity, deadline, time_frame, category, status)

    def write_tasks_to_csv(self, tasks, filename):
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Description', 'Severity', 'Deadline (Weekday)', 'Time Frame', 'Category', 'Status'])
                for task in tasks:
                    writer.writerow([task.description, task.severity.value, task.deadline.value,
                                     task.time_frame.value, task.category.value, task.status.value])
            print(f"Tasks have been written to {filename}.")
        except Exception as e:
            print(f"Error writing to CSV: {e}")


def main():
    print("My ToDo List Project")
    task_manager = TaskManager()

    while True:
        command = input("Type 'exit' to quit or press Enter to continue: ").strip().lower()
        if command == 'exit':
            print("Exiting the program.")
            break

        task = TaskIO().get_task_from_input()
        task_manager.add_task(task)

        if task_manager.tasks:
            csv_file_name = 'Mytask01.csv'
            TaskIO().write_tasks_to_csv(task_manager.tasks, csv_file_name)

            time_frame = TaskIO().get_valid_enum_input(
                "Which time frame would you like to inspect? (today/this week/this month): ", TimeFrame)
            category_input = input("Enter category to filter by (or press Enter to skip): ").strip()
            category = TaskCategory[category_input.upper()] if category_input else None

            filtered_tasks = task_manager.filter_tasks(time_frame, category)
            if filtered_tasks:
                print(f"Tasks for {time_frame.value}{' in category: ' + category.value if category else ''}:")
                for task in filtered_tasks:
                    print(task)
            else:
                print(
                    f"No tasks found for {time_frame.value}{' in category: ' + (category.value if category else 'N/A')}.")

            summary = task_manager.summarize_status()
            print("Status Summary:")
            for status, count in summary.items():
                print(f"Status: {status}, Count: {count}")
        else:
            print("No valid tasks to write.")


if __name__ == "__main__":
    main()