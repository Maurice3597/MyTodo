FILEPATH= 'todos.txt'

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_todos(todo_arg, filepath=FILEPATH):
    with open(filepath, 'w') as local_file:
        local_file.writelines(todo_arg)