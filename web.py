import streamlit as st
import functions as fn


todos = fn.read_file()

def add_todo() :
    local_todo = st.session_state['new_todo'] + '\n'
    todos.append(local_todo)
    fn.write_file('test.txt' , todos)


st.title("Hello Users")
st.subheader("Todo web app")

bool_list = []

for todo in todos :
    x = st.checkbox(todo)
    bool_list.append(x)

st.text_input(label='' , placeholder='Enter a todo...' , 
              on_change=add_todo , key='new_todo')

print(bool_list)

for index,item in enumerate(bool_list) :
    if item :
        todos.pop(index)
        fn.write_file('test.txt' , todos)
        st.rerun()