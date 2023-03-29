import streamlit as st
import funcitons


places = funcitons.list_place()

def add_place():
    place = st.session_state["new_place"] + "\n"
    places.append(place)
    funcitons.write_place(places)

st.title("Travel Diary")
st.subheader("Go to experience!")
st.write("To go:")


for index, place in enumerate(places):
    checkbox = st.checkbox(place, key=place)
    if checkbox:
        places.pop(index)
        funcitons.write_place(places)
        del st.session_state[place]
        st.experimental_rerun()



st.text_input(label="", placeholder="Add a place...",
              on_change=add_place, key="new_place")



