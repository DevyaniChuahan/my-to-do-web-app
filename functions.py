def get_todos(filepath="todos.txt"):
    """Read a file and returns a list of to do items."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath="todos.txt"):
    """Add a new todo to a list of to do items."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)