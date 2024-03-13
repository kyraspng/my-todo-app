FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH): # the element within the bracket is called 'parameter' of the function
    """ This is called 'doc-string' """
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

# the second function behaves like a procedure, and nothing is required to be returned.
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:  # w: write; r: read # Inherently, the 'w' will overwrite the file.
        file.writelines(todos_arg)

# IF conditional block
if __name__ == "__main__":
    print("Hello")
    print(get_todos())