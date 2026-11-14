def add_task(tasks, name):
    """Add a task name to the tasks list."""
    if name.strip() == "":
        print("Invalid task name")
        return tasks
    tasks.append(name)
    return tasks
