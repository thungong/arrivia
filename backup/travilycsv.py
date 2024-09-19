import streamlit as st
import pandas as pd

# Set app title and icon
st.set_page_config(page_title="Travily CSV", page_icon="app_icon.png")

# Streamlit app
#st.set_page_config(page_icon="app_icon.png")
st.title("Travily Account Creator - V1.29")

# Validate the uploaded file to ensure it has the correct columns for Travily
def validate_travily_file(df):
    required_columns = ["Account Status", "Owner ID", "First Name", "Last Name", "Billing Country", "Email", "Mobile", "Primary Contact Person", "Secondary Contact Person"]
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        st.error(f"The uploaded file is incorrect for Travily: Missing columns: {', '.join(missing_columns)}. Upload correct file then.")
        return False
    return True

# Function to transform data for Primary CSV
def transform_primary_data(df):
    transformed_data = []
    primary_df = df[df['Primary Contact Person'].isin([True, 1, 'TRUE', 'True'])]

    for _, row in primary_df.iterrows():
        certificate_number = "FZRQZQM6"  # Fixed value
        authorization_code = "HTQ4T2T4"  # Fixed value
        third_party_id = row["Owner ID"]  # Using 'Owner ID' as 'ThirdPartyId'
        user_name = row["Email"]
        first_name = row["First Name"]
        last_name = row["Last Name"]
        country_code = row["Billing Country"]
        email_address = row["Email"]
        telephone = row["Mobile"]
        user_account_token = ""  # Empty UserAccountToken

        new_row = {
            "CertificateNumber": certificate_number,
            "AuthorizationCode": authorization_code,
            "ThirdPartyId": third_party_id,
            "UserName": user_name,
            "FirstName": first_name,
            "LastName": last_name,
            "CountryCode": country_code,
            "EmailAddress": email_address,
            "Telephone": telephone,
            "UserAccountToken": user_account_token
        }
        transformed_data.append(new_row)

    transformed_df = pd.DataFrame(transformed_data)
    return transformed_df

# Function to transform data for Travily CSV (Secondary)
def transform_travily_data(df):
    transformed_data = []
    secondary_df = df[df['Secondary Contact Person'].isin([True, 1, 'TRUE', 'True'])]

    for _, row in secondary_df.iterrows():
        third_party_id = row["Owner ID"]  # Using 'Owner ID' as 'ThirdPartyId'
        user_account_token = ""  # Empty UserAccountToken
        email_address = row["Email"]
        user_name = row["Email"]
        first_name = row["First Name"]
        last_name = row["Last Name"]
        country_code = row["Billing Country"]
        telephone = row["Mobile"]

        new_row = {
            "ThirdPartyId": third_party_id,
            "UserAccountToken": user_account_token,
            "EmailAddress": email_address,
            "UserName": user_name,
            "FirstName": first_name,
            "LastName": last_name,
            "CountryCode": country_code,
            "Telephone": telephone
        }
        transformed_data.append(new_row)

    transformed_df = pd.DataFrame(transformed_data)
    return transformed_df

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("Column Names in the Uploaded File:", df.columns.tolist())  # Display the column names to check

    if validate_travily_file(df):
        st.write("---")
        st.header("Original Data")
        st.dataframe(df)

        st.write("---")
        st.header("Select Operation")

        operation = st.selectbox(
            "Choose the operation you want to perform:",
            ("Select an option", "Transform Data for Primary CSV", "Transform Data for Secondary CSV")
        )

        if operation == "Transform Data for Primary CSV":
            primary_transformed_df = transform_primary_data(df)
            if primary_transformed_df is not None:
                st.write("### Transformed Data for Primary CSV")
                st.dataframe(primary_transformed_df)

                primary_csv = primary_transformed_df.to_csv(index=False)
                st.download_button(
                    label="Download Primary CSV",
                    data=primary_csv,
                    file_name="Travily_primary_member_data.csv",
                    mime="text/csv",
                )

        elif operation == "Transform Data for Secondary CSV":
            travily_transformed_df = transform_travily_data(df)
            if travily_transformed_df is not None:
                st.write("### Transformed Data for Secondary CSV")
                st.dataframe(travily_transformed_df)

                travily_csv = travily_transformed_df.to_csv(index=False)
                st.download_button(
                    label="Download Travily CSV",
                    data=travily_csv,
                    file_name="Travily_secondary_member_data.csv",
                    mime="text/csv",
                )

        else:
            st.info("Please select an operation to perform.")
