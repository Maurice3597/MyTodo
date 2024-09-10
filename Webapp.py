import streamlit as st
from streamlit import checkbox, session_state

import functions as fxns

todos = fxns.get_todos()

def add_todo():
    Todo = st.session_state["New_todo"] + "\n"
    todos.append(Todo)
    fxns.write_todos(todos)

st.title("MY TODO APP")
st.subheader("your favourite TODO online app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

st.text_input(label='ADD TODO', placeholder='Add todo',
              label_visibility="collapsed",
              on_change=add_todo, key= "New_todo" )

edit_btn = st.button('Edit', key='edit')
delete_btn = st.button('Delete', key='delete')
clear_btn = st.button('Clear', key='clear')

for todo in todos:
    if clear_btn:
        todos.clear()
        fxns.write_todos(todos)
        del session_state[todo]
        st.rerun()

for index,todo in enumerate(todos):
    if checkbox:
        todos.pop(index)
        fxns.write_todos(todos)
        del session_state[todo]
        st.rerun()
