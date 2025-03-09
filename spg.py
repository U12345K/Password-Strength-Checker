import re
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Password Strength Checker", page_icon=":smiley:", layout="centered")

# Apply custom styling
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton {width:50%; background-color: #4CAF50; color: white; font-size: 18px;}
    .stButton:hover {background-color: #45a049;}
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("Password Strength Checker")
st.write("Enter your password to check its strength")

# Function to check password strength
def check_password(password):
    score = 0
    feedback = []

    # Check for length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Bad: Password is less than 8 characters long")

    # Check for uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Bad: Password must contain both uppercase and lowercase letters")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Bad: Password must contain at least one digit")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Bad: Password must contain at least one special character")

    # Display the result
    if score == 4:
        st.success("Strong Password")
    elif score == 3:
        st.info("Medium Password")
    else:
        st.error("Weak Password")

    # Display feedback if applicable
    if feedback:
        with st.expander("Feedback"):
            for item in feedback:
                st.write(item)

# Input field for password
password = st.text_input(
    "Enter your password", 
    type="password",
    help="Password must be at least 8 characters long and contain both uppercase and lowercase letters, at least one digit, and at least one special character"
)

# Button to check password strength
if st.button("Check Password"):
    if password:
        check_password(password)
    else:
        st.warning("Please enter a password")

st.markdown("<div class='footer'>Developed by UMAR KHAN</div>", unsafe_allow_html=True)