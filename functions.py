FILEPATH = 'tasks.txt'

def get_tasks(filepath=FILEPATH):
    """ Reads a text file and returns a list of to-do items."""
    with open(filepath, 'r') as files_local:
        tasks_local = files_local.readlines()
    return tasks_local


def write_tasks(task, filepath=FILEPATH):
    """Writes a list of amended to-do items to a text file"""
    with open(filepath, 'w') as file:
        file.writelines(task)


if __name__ == "__main__":
    print("hello")
