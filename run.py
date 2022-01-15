import streamlit as st

from py_playground import builder as bob

#### Title
st.title("Welcome to the platform builder!")
st.subheader("My name is Bob, let me assist you.")

#### Planks
st.header("First I'll need some information about the wood you have")

st.text("I hear you bought some wood?")

col1, col2, col3 = st.columns(3)

with col1:
    length = st.number_input("Plank length", min_value=0)
with col2:
    width = st.number_input("Plank width", min_value=0)
with col3:
    height = st.number_input("Plank height", min_value=0)

total = st.number_input("How many planks did you get?", min_value=0)

planks = [
    bob.Plank(
        length=length,
        width=width,
        height=height,
    )
] * total

#### Platform
st.header("Tell us about the platform you're building")
st.subheader("What are the dimensions of the platform ")

col1, col2 = st.columns(2)

with col1:
    length = st.number_input("Length", min_value=0)
with col2:
    width = st.number_input("Width", min_value=0)

st.subheader("Bob will post the results for you here")

platform = bob.Platform(width=width, length=length, planks=planks)

if st.button("Calculate!"):
    st.text(
        "Here's the points along the short sides of your platform where you should drill:"
    )
    st.table(
        platform.calculate_plank_positions(),
    )
