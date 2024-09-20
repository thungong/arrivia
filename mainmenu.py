import streamlit as st
import webbrowser

# Set app title and icon
st.set_page_config(page_title="Menu: Member MGMT", page_icon="app_icon.png")

# Streamlit app
st.title("CSV Preparation Tool - Version 2")

# Main menu
st.header("Select the Data Transformation Tool")

option = st.selectbox(
    "Choose the tool you need:",
    ("Select an option", "MT&L CSV Preparation", "Travily CSV Preparation", "Arrivia API Tool")
)

if option == "MT&L CSV Preparation":
    st.write("You have selected the MT&L CSV Preparation tool.")
    if st.button("Go to MT&L CSV Preparation"):
        webbrowser.open_new_tab("https://mtlcsv.streamlit.app/")

elif option == "Travily CSV Preparation":
    st.write("You have selected the Travily CSV Preparation tool.")
    if st.button("Go to Travily CSV Preparation"):
        webbrowser.open_new_tab("https://travilycsv.streamlit.app/")

elif option == "Arrivia API Tool":
    st.write("You have selected the API Tool.")
    if st.button("Go to API Tool"):
        webbrowser.open_new_tab("https://avcapitool-na6yhruzp7ucyappmjjklt3.streamlit.app/")

else:
    st.info("Please select a tool to proceed.")
