import streamlit as st
import functions as func

todo_list = func.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todo_list.append(new_todo)
    func.write_todos(todo_list)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        func.write_todos(todo_list)
        del st.session_state[todo]

        # this basically reruns the script/refreshes page
        st.experimental_rerun()


st.text_input(label="Enter todo", label_visibility="hidden", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")


# # prints to the webpage like a console
# # should leave here during development
# st.session_state
