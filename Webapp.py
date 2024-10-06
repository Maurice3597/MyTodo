import streamlit as st
import functions as fxns


# Initialize or update the todo list filepath
fxns.create_filepath()
todos = fxns.get_todos()  # Fetch existing todos from a data source


# function to add a new todo item from the input to the list
def add_todo():
    if st.session_state["New_todo"]:  # Check if the input is not empty
        todo = st.session_state["New_todo"]
        todos.append(todo + "\n")  # Append the new todo with new line
        fxns.write_todos(todos)  # Save updated todos to the data source
        st.session_state["New_todo"] = ""  # Clear the input box after adding


# Setting up the page title and a subheader
st.title("MY TODO APP")
st.subheader("Your favourite TODO online app")

# Display existing todos with checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f'checkbox{index +1}')  # Use index for unique keys

# Input for new todo items
st.text_input(label='ADD TODO', placeholder='Add todo',
              label_visibility="collapsed",
              on_change=add_todo, key="New_todo")

# Buttons for clearing todos
clear_btn = st.button('Clear All', key='clear')

# Clear all todos if the 'Clear' button is pressed
if clear_btn:
    todos.clear()
    fxns.write_todos(todos)
    # Clear relevant session state keys
    for todo_key in list(st.session_state.keys()):
        if todo_key.startswith('checkbox'):
            del st.session_state[todo_key]
    st.rerun() # refreshes the app

# Process deleting todos (based on checked items)
delete_btn = st.button('Delete', key='delete')
if delete_btn:
    # Collect all indices of checked items
    checked_indices = [index for index in range(len(todos))\
                       if st.session_state.get(f'checkbox{index + 1}', False)]

    # Remove todos in reverse order to avoid index shifting issues
    for index in reversed(checked_indices):
        print(index)
        todos.pop(index)  # Remove the todo at the index

    fxns.write_todos(todos)  # Update the data source with remaining todos

    # Clear checkbox states for deleted items
    for index in checked_indices:
        del st.session_state[f'checkbox{index + 1}']
    st.rerun()  # Refresh the app

#st.session_state
