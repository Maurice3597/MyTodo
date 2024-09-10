import streamlit as st

# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Function to increment the counter
def increment_counter():
    st.session_state.counter += 1

# Display the current counter value
st.write(f"Counter: {st.session_state.counter}")

# Button to increment the counter
if st.button('Increment'):
    increment_counter()
