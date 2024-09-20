import streamlit as st
import pandas as pd

# Set app title and icon
st.set_page_config(page_title="MT&L CSV", page_icon="app_icon.png")

# Streamlit app
st.title("MT&L Member Account Creator and Upgrader - V1.35")

# Define the correct mapping for Primary Member Creation
primary_mapping = {
    "ELITE JADE": ("5M6NFXNQ", "3DL6BKRB"),
    "ELITE RUBY": ("DS3B5R8D", "SNZ2M68S"),
    "ELITE DIAMOND": ("99LC6JT5", "C9LSC8HG"),
    "ELITE PLATINUM": ("ZDVR3WDK", "DLDSXPQ9"),
    "ELITE ROYAL": ("J8GCV8D9", "TDRVF8Z9"),
    "OPAL": ("5M6NFXNQ", "3DL6BKRB"),
    "PEARL": ("DS3B5R8D", "SNZ2M68S"),
    "EMERALD": ("99LC6JT5", "C9LSC8HG"),
    "PRESTIGE": ("ZDVR3WDK", "DLDSXPQ9"),
    "SAPPHIRE": ("J8GCV8D9", "TDRVF8Z9"),
}

# Define the mapping for Upgrade
upgrade_mapping = {
    "ELITE JADE": ("HT8V3968", "4Z67JZ5K"),
    "ELITE RUBY": ("B83VH4HH", "KLRV4WJK"),
    "ELITE DIAMOND": ("XFG7MVRH", "PLQ6VXTF"),
    "ELITE PLATINUM": ("PXR25N36", "4DB3D46Z"),
    "ELITE ROYAL": ("V59P83HM", "VQW2B4WF"),
    "OPAL": ("HT8V3968", "4Z67JZ5K"),
    "PEARL": ("B83VH4HH", "KLRV4WJK"),
    "EMERALD": ("XFG7MVRH", "PLQ6VXTF"),
    "PRESTIGE": ("PXR25N36", "4DB3D46Z"),
    "SAPPHIRE": ("V59P83HM", "VQW2B4WF"),
}

# Validate the uploaded file for the appropriate operation
def validate_mtl_file(df):
    if set(["Owner ID", "First Name", "Last Name", "Billing Country", "Email", "Phone", "Mobile", "Public Contract Names", "Primary Contact Person"]).issubset(df.columns):
        return "Transform Primary & Secondary Data to CSV"
    elif set(["Owner ID", "Prior Public Contract Name", "Public Contract Names"]).issubset(df.columns):
        return "Transform Data for Upgrade"
    else:
        st.error("The uploaded file is incorrect for MT&L: Missing necessary columns.")
        return None

# Function to transform the data for Primary Member Account creation
def transform_primary_data(df):
    ws_user_name = "mytravel.lifestyle"
    ws_password = "Ga1N0n1GfNhsDpmlhxag"
    partner_id = 287
    default_password = "AVCTH2024!"

    transformed_data = []

    primary_df = df[df['Primary Contact Person'].isin([True, 1, 'TRUE', 'True'])]

    for _, row in primary_df.iterrows():
        owner_id = row["Owner ID"]
        first_name = row["First Name"]
        last_name = row["Last Name"]
        country_code = row["Billing Country"]
        email = row["Email"]
        telephone = row["Phone"] if pd.notna(row["Phone"]) else row["Mobile"]
        member_class = row["Public Contract Names"].strip().upper()

        certificate_number, authorization_code = primary_mapping.get(member_class, ("", ""))

        new_row = {
            "WsUserName": ws_user_name,
            "WsPassword": ws_password,
            "PartnerId": partner_id,
            "CertificateNumber": certificate_number,
            "AuthorizationCode": authorization_code,
            "ThirdPartyId": owner_id,
            "UserName": email,
            "Password": default_password,
            "FirstName": first_name,
            "LastName": last_name,
            "Telephone": telephone,
            "CountryCode": country_code,
            "EmailAddress": email,
            "EmailOptIn": "true",
            "UserAccountToken": ""  # Empty UserAccountToken
        }
        transformed_data.append(new_row)

    transformed_df = pd.DataFrame(transformed_data)
    transformed_df = transformed_df.drop_duplicates(subset=["ThirdPartyId"])

    return transformed_df

# Function to transform the data for Upgrade
def transform_upgrade_data(df):
    ws_user_name = "mytravel.lifestyle"
    ws_password = "Ga1N0n1GfNhsDpmlhxag"
    partner_id = 287

    transformed_data = []

    for _, row in df.iterrows():
        owner_id = row["Owner ID"]
        member_class = row["Public Contract Names"].strip().upper()

        certificate_number, authorization_code = upgrade_mapping.get(member_class, ("", ""))

        new_row = {
            "WsUserName": ws_user_name,
            "WsPassword": ws_password,
            "PartnerId": partner_id,
            "ThirdPartyId": owner_id,
            "CertificateNumber": certificate_number,
            "AuthorizationCode": authorization_code,
            "UserAccountToken": ""  # Empty UserAccountToken
        }
        transformed_data.append(new_row)

    transformed_df = pd.DataFrame(transformed_data)
    transformed_df = transformed_df.drop_duplicates(subset=["ThirdPartyId"])

    return transformed_df

# File upload functionality
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("Column Names in the Uploaded File:", df.columns.tolist())

    st.write("---")
    st.header("Original Data")
    st.dataframe(df)

    operation = validate_mtl_file(df)

    if operation:
        if operation == "Transform Primary & Secondary Data to CSV":
            primary_transformed_df = transform_primary_data(df)
            if primary_transformed_df is not None:
                st.write("### Transformed Data for Primary Member Accounts (Filtered)")
                st.dataframe(primary_transformed_df)

                primary_csv = primary_transformed_df.to_csv(index=False)
                st.download_button(
                    label="Download Primary Member CSV",
                    data=primary_csv,
                    file_name="MTL_primary_member_data.csv",
                    mime="text/csv",
                )

                secondary_df = df[df['Secondary Contact Person'].isin([True, 1, 'TRUE', 'True'])]

                if not secondary_df.empty:
                    secondary_data = []

                    for _, row in secondary_df.iterrows():
                        owner_id = row["Owner ID"]
                        first_name = row["First Name"]
                        last_name = row["Last Name"]
                        country_code = row["Billing Country"]
                        email = row["Email"]
                        telephone = row["Phone"] if pd.notna(row["Phone"]) else row["Mobile"]

                        new_row = {
                            "WsPassword": "Ga1N0n1GfNhsDpmlhxag",
                            "PartnerId": 287,
                            "ThirdPartyId": owner_id,
                            "UserAccountToken": "",  # Empty UserAccountToken
                            "EmailAddress": email,
                            "UserName": email,
                            "Password": "AVCTH2024!",
                            "FirstName": first_name,
                            "LastName": last_name,
                            "CountryCode": country_code,
                            "Telephone": telephone,
                            "EmailOptIn": "TRUE"
                        }
                        secondary_data.append(new_row)

                    secondary_transformed_df = pd.DataFrame(secondary_data)
                    st.write("### Transformed Data for Secondary Member Accounts (Filtered)")
                    st.dataframe(secondary_transformed_df)

                    secondary_csv = secondary_transformed_df.to_csv(index=False)
                    st.download_button(
                        label="Download Secondary Member CSV",
                        data=secondary_csv,
                        file_name="MTL_secondary_member_data.csv",
                        mime="text/csv",
                    )
                else:
                    st.warning("No data found for Secondary Members.")

        elif operation == "Transform Data for Upgrade":
            upgrade_transformed_df = transform_upgrade_data(df)
            if upgrade_transformed_df is not None:
                st.write("### Transformed Data for Upgrade")
                st.dataframe(upgrade_transformed_df)

                upgrade_csv = upgrade_transformed_df.to_csv(index=False)
                st.download_button(
                    label="Download Upgrade CSV",
                    data=upgrade_csv,
                    file_name="upgrade_data.csv",
                    mime="text/csv",
                )
