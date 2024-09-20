import streamlit as st

# Set app title and icon
st.set_page_config(page_title="Member Data Management", page_icon="app_icon.png")

# Streamlit app
st.title("Member Data Transformation Tools - Version 2")

# Main menu
st.header("Select a Data Transformation or API Tool")

option = st.selectbox(
    "Choose the tool you need:",
    ("Select an option", "MT&L CSV Preparation", "Travily CSV Preparation", "Arrivia API Tool")
)

if option == "MT&L CSV Preparation":
    st.write("You have selected the MT&L CSV Preparation tool.")
    st.markdown(
        '[Go to MT&L CSV Preparation](https://mtlcsv.streamlit.app/)', 
        unsafe_allow_html=True
    )

elif option == "Travily CSV Preparation":
    st.write("You have selected the Travily CSV Preparation tool.")
    st.markdown(
        '[Go to Travily CSV Preparation](https://travilycsv.streamlit.app/)', 
        unsafe_allow_html=True
    )

elif option == "Arrivia API Tool":
    st.write("You have selected the Arrivia API tool.")
    st.markdown(
        '[Go to Arrivia API Tool](https://avcapitool-na6yhruzp7ucyappmjjklt3.streamlit.app/)', 
        unsafe_allow_html=True
    )

else:
    st.info("Please select a tool to proceed.")
