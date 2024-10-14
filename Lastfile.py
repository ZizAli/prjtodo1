import csv
print( "My To Do List")
def get_tasks_from_input():
    my_task = input("Add tasks (format: description, severity, deadline): \n")
    tasks = my_task.split(';')
    valid_tasks = []

    for todo, text in enumerate(tasks, start=1):
        task = text.split(',')
        if len(task) == 3:
            description = task[0].strip()
            severity = task[1].strip()
            deadline = task[2].strip()
            valid_tasks.append((description, severity, deadline))
            print(f"{todo}. [Severity: {severity}] [Description: {description}] [Deadline: {deadline}]")
        else:
            print(f"{todo}. Invalid entry format: {text.strip()}")

    return valid_tasks


def write_tasks_to_csv(tasks, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Description', 'Severity', 'Deadline'])
        writer.writerows(tasks)


def main():
    print("My ToDo List Project")
    tasks = get_tasks_from_input()

    if tasks:
        csv_file_name = 'Mytask.csv'
        write_tasks_to_csv(tasks, csv_file_name)
        print(f"Tasks have been written to {csv_file_name}.")
    else:
        print("No valid tasks to write.")


if __name__ == "__main__":
    main()
