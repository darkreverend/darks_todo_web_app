FILEPATH = "todos.txt"




def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of todo items.
     This function contains a default parameter for the file name.
     Can be overridden by adding the argument to the function call filename="whatever.txt"
    """
    with open(filepath, "r") as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todos(todo_list_arg, filepath=FILEPATH):
    """ Write a todo item in the text file
     This function contains a default parameter for the file name.
     Can be overridden by adding the argument to the function call filename="whatever.txt"
     """
    with open(filepath, "w") as file_local:
        file_local.writelines(todo_list_arg)


print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
