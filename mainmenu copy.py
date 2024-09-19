import streamlit as st
import subprocess

# Streamlit app
st.title("CSV Preparation Tool")

# Main menu
st.header("Select the Data Transformation Tool")

option = st.selectbox(
    "Choose the tool you need:",
    ("Select an option", "MT&L CSV Preparation", "Travily CSV Preparation")
)

if option == "MT&L CSV Preparation":
    st.write("You have selected the MT&L CSV Preparation tool.")
    if st.button("Go to MT&L CSV Preparation"):
        subprocess.run(["streamlit", "run", "mtlcsvdev.py"])

elif option == "Travily CSV Preparation":
    st.write("You have selected the Travily CSV Preparation tool.")
    if st.button("Go to Travily CSV Preparation"):
        subprocess.run(["streamlit", "run", "travilycsv.py"])

else:
    st.info("Please select a tool to proceed.")
