import streamlit as st
import mtlcsv
import travilycsv
import forapi

# Set app title and icon
st.set_page_config(page_title="Member MGMT", page_icon="app_icon.png")

# Apply custom CSS for the background and text color
corporate_bg_color = "#003366"
text_color = "white"

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
        background-color: #0055a5;
        color: white;
    }}
    .stButton button:hover {{
        background-color: #004080;
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("CSV Preparation Tool - Version 2")

option = st.selectbox(
    "Choose the tool you need:",
    ("Select an option", "MT&L CSV Preparation", "Travily CSV Preparation", "Creation API")
)

if option == "MT&L CSV Preparation":
    mtlcsv.run()

elif option == "Travily CSV Preparation":
    travilycsv.run()

elif option == "Creation API":
    forapi.run()

else:
    st.info("Please select a tool to proceed.")
