import streamlit as st
import subprocess

# Set app title and icon
st.set_page_config(page_title="Member MGMT", page_icon="app_icon.png")

# Define corporate background color and text color
corporate_bg_color = "#003366"  # Example background color, replace with your corporate color
text_color = "white"  # Set text color to white for better visibility

# Apply custom CSS for the background and text color
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {corporate_bg_color};
        color: {text_color};
    }}
    h1, h2, h3, h4, h5, h6, p, label {{
        color: {text_color};
    }}
    .stSelectbox label {{
        color: {text_color};
    }}
    .stButton button {{
        background-color: #0055a5;  /* Example button color */
        color: white;
    }}
    .stButton button:hover {{
        background-color: #004080;  /* Example button hover color */
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app
st.title("CSV Preparation Tool - Version 2")

# Main menu
st.header("Select the Data Transformation Tool")

option = st.selectbox(
    "Choose the tool you need:",
    ("Select an option", "MT&L CSV Preparation", "Travily CSV Preparation", "Creation API")
)

if option == "MT&L CSV Preparation":
    st.write("You have selected the MT&L CSV Preparation tool.")
    if st.button("Go to MT&L CSV Preparation"):
        subprocess.run(["streamlit", "run", "mtlcsv.py"])

elif option == "Travily CSV Preparation":
    st.write("You have selected the Travily CSV Preparation tool.")
    if st.button("Go to Travily CSV Preparation"):
        subprocess.run(["streamlit", "run", "travilycsv.py"])

elif option == "Creation API":
    st.write("You have selected the Creation API tool.")
    if st.button("Go to Creation API"):
        subprocess.run(["streamlit", "run", "forapi.py"])

else:
    st.info("Please select a tool to proceed.")
