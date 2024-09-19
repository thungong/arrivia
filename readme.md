# Member Management CSV Preparation Tool

This is a Streamlit-based application for preparing CSV files and sending SOAP API requests for member management. The tool supports two systems: **MT&L** and **Travily**, allowing the creation of primary and secondary member accounts, as well as membership upgrades.

## Features

- **MT&L CSV Preparation**: Allows users to upload Excel files and generate CSV files for primary and secondary members, as well as perform upgrades.
- **Travily CSV Preparation**: Allows users to upload Excel files and generate CSV files for primary and secondary members.
- **Creation API**: Provides an interface for sending SOAP API requests to the **MT&L** and **Travily** systems for membership management.

## Requirements

To install the dependencies, ensure you have `Python 3.x` installed, and then run:

```bash
pip install -r requirements.txt
Required Packages
pandas==2.2.1
requests==2.31.0
streamlit==1.33.0
python-dotenv==1.0.1
openpyxl==3.1.2
xlrd==2.0.1

# How to Use
1. Main Menu
When you launch the app, you will be prompted to select one of the three available tools:

MT&L CSV Preparation: For creating and preparing MT&L member data CSV files.
Travily CSV Preparation: For creating and preparing Travily member data CSV files.
Creation API: For sending SOAP requests to manage member accounts.
2. MT&L CSV Preparation
Upload an Excel file containing the required columns.
Select whether to transform data for primary or secondary members, or perform an upgrade.
Download the resulting CSV file.
3. Travily CSV Preparation
Similar to MT&L, upload an Excel file and select the transformation operation.
Download the generated CSV file for primary or secondary members.
4. Creation API
Log in with your credentials.
Choose the system (MT&L or Travily) and the action you want to perform.
You can either input the required fields manually or upload a CSV file.
Submit the SOAP request and view the responses.
Running the App
To run the app, use the following command:
streamlit run mainmenu.py
