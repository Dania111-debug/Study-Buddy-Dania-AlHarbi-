def add_task(tasks, name):
    """Add a task name to the tasks list."""
    if name.strip() == "" or len(name) > 30:
        print("Invalid task name")
        return tasks
    tasks.append(name)
    return tasks