# Constants
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Reads a textfile and returns the list of todo items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes the list of todos to a text file.
    """
    with open(filepath, "w") as local_file:
        local_file.writelines(todos_arg)


# print(__name__)  # this will print "functions" when you run it main.py

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
