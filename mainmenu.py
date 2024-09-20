import streamlit as st

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
        st.markdown("[Click here to open MT&L CSV Preparation](https://mtlcsv.streamlit.app/)", unsafe_allow_html=True)

elif option == "Travily CSV Preparation":
    st.write("You have selected the Travily CSV Preparation tool.")
    if st.button("Go to Travily CSV Preparation"):
        st.markdown("[Click here to open Travily CSV Preparation](https://travilycsv.streamlit.app/)", unsafe_allow_html=True)

elif option == "Arrivia API Tool":
    st.write("You have selected the API Tool.")
    if st.button("Go to API Tool"):
        st.markdown("[Click here to open Arrivia API Tool](https://avcapitool-na6yhruzp7ucyappmjjklt3.streamlit.app/)", unsafe_allow_html=True)

else:
    st.info("Please select a tool to proceed.")
