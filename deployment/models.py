import streamlit as st
from Introduction import introduction_page  # Import your page functions
from NN_models import nn_models_page
from classification import classification_page  # Renamed for clarity
from Aboutme import about_me_page

# Set page config
st.set_page_config(page_title="Handwritten Alphabet Classification", page_icon=":books:", initial_sidebar_state= "collapsed", layout="wide" )

def local_css(file_name):
    """Function to load and apply custom CSS"""
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Import custom CSS for button styling
local_css("style.css")

# Title with gradient background
st.markdown("""
    <h1 style="background: linear-gradient(45deg, #f39c12, #eb52ae); -webkit-background-clip: text; color: transparent; text-align:center; margin-bottom:40px;">
    Handwritten Alphabet Classification
    </h1>
    """, unsafe_allow_html=True)


# Initialize session state for button clicks (Important!)
# Initialize page in session state (Crucial!)
if "page" not in st.session_state:
    st.session_state.page = "home"


# This can be moved into a separate function for better structure if needed
if "home_clicked" not in st.session_state:
    st.session_state.home_clicked = True
if "nn_clicked" not in st.session_state:
    st.session_state.nn_clicked = False
if "classification_clicked" not in st.session_state:
    st.session_state.classification_clicked = False
if "about_clicked" not in st.session_state:
    st.session_state.about_clicked = False

# Sidebar navigation using buttons
with st.sidebar:
    st.header("Navigation")
    if st.button(":house: Home", key="home_button"):
        st.session_state.home_clicked = True
        st.session_state.nn_clicked = False
        st.session_state.classification_clicked = False
        st.session_state.about_clicked = False
    if st.button(":books: Models", key="nn_button"):
        st.session_state.home_clicked = False
        st.session_state.nn_clicked = True
        st.session_state.classification_clicked = False
        st.session_state.about_clicked = False
    if st.button(":mag: Classification", key="classification_button"):  # More descriptive button label
        st.session_state.home_clicked = False
        st.session_state.nn_clicked = False
        st.session_state.classification_clicked = True
        st.session_state.about_clicked = False
    if st.button(":technologist: About Me", key="about_button"):
        st.session_state.home_clicked = False
        st.session_state.nn_clicked = False
        st.session_state.classification_clicked = False
        st.session_state.about_clicked = True

# Function to load pages (using session state)
def load_page():
    """Load the appropriate page based on the session state"""
    if st.session_state.home_clicked:
        introduction_page()
    elif st.session_state.about_clicked:
        about_me_page()
    elif st.session_state.nn_clicked:
        nn_models_page()
    elif st.session_state.classification_clicked:
        classification_page()  # Call the prediction page function

# Display selected page
load_page()

# Footer
st.markdown("<div class='stFooter'>© 2024 Adithya Vardhan Reddy | Kapil IT Hub</div>", unsafe_allow_html=True)