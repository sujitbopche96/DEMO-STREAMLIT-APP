import streamlit as st

# Title
st.title("🔐 Login Form Example")

# Header
st.header("Welcome to the Secure Portal")

# Subheader
st.subheader("Please enter your credentials")

# Markdown (instructions)
st.markdown("👉 Enter your **username** and **password** below to continue.")

# Input fields
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Button
if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("✅ Login successful!")
    else:
        st.error("❌ Invalid username or password")

# Code block (for demonstration)
st.code(
    """if username == "admin" and password == "1234":
    st.success("Login successful!")
else:
    st.error("Invalid username or password")""",
    language="python"
)
