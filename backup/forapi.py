import streamlit as st
import pandas as pd
import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os
import time

load_dotenv()

users = {
    "thungong": os.getenv("USER1_PASSWORD"),
    "user2": os.getenv("USER2_PASSWORD"),
    "user3": os.getenv("USER3_PASSWORD"),
    "club": os.getenv("CLUB_PASSWORD")
}

# Set app title and icon
st.set_page_config(page_title="Arrivia Member MGMT", page_icon="app_icon.png")

# Membership types and their corresponding certificate and authorization codes for Upgrade or Downgrade
membership_types = {
    "ELITE JADE": {"Cert": "HT8V3968", "Auth": "4Z67JZ5K"},
    "ELITE RUBY": {"Cert": "B83VH4HH", "Auth": "KLRV4WJK"},
    "ELITE DIAMOND": {"Cert": "XFG7MVRH", "Auth": "PLQ6VXTF"},
    "ELITE PLATINUM": {"Cert": "PXR25N36", "Auth": "4DB3D46Z"},
    "ELITE ROYAL": {"Cert": "V59P83HM", "Auth": "VQW2B4WF"},
    "OPAL": {"Cert": "HT8V3968", "Auth": "4Z67JZ5K"},
    "PEARL": {"Cert": "B83VH4HH", "Auth": "KLRV4WJK"},
    "EMERALD": {"Cert": "XFG7MVRH", "Auth": "PLQ6VXTF"},
    "PRESTIGE": {"Cert": "PXR25N36", "Auth": "4DB3D46Z"},
    "SAPPHIRE": {"Cert": "V59P83HM", "Auth": "VQW2B4WF"}
}

# Define SOAP endpoints for each system
endpoints = {
    "MT&L": {
        "CreatePrimary": "https://ws.ourvacationstore.com/membership/member.asmx",
        "UpgradeMembership": "https://ws.ourvacationstore.com/membership/member.asmx",
        "CreateSecondary": "https://ws.ourvacationstore.com/membership/member.asmx",
        "UpdateUserAccount": "https://ws.ourvacationstore.com/membership/member.asmx",
        "UpdateUserPhone": "https://ws.ourvacationstore.com/membership/member.asmx",
        "GetUserAccountToken": "https://ws.ourvacationstore.com/membership/member.asmx",
        "UpdateThirdPartyId": "https://ws.ourvacationstore.com/membership/member.asmx",
        "GetMembershipInformation": "https://ws.ourvacationstore.com/membership/member.asmx"
    },
    "Travily": {
        "CreateMembership": "https://ws.ourvacationstore.com/membership/member.asmx",
        "CreateSecondaryMember": "https://ws.ourvacationstore.com/membership/member.asmx",
        "UpdateUserAccount": "https://ws.ourvacationstore.com/membership/member.asmx",
        "UpdateUserPhone": "https://ws.ourvacationstore.com/membership/member.asmx",
        "GetUserAccountToken": "https://ws.ourvacationstore.com/membership/member.asmx",
        "UpdateThirdPartyId": "https://ws.ourvacationstore.com/membership/member.asmx",
        "GetMembershipInformation": "https://ws.ourvacationstore.com/membership/member.asmx"
    }
}

# Payload templates for each action and system
payloads = {
    "MT&L": {
        "CreatePrimary": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <CreateMembershipNG xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>mytravel.lifestyle</WsUserName>
            <WsPassword>Ga1N0n1GfNhsDpmlhxag</WsPassword>
            <PartnerId>287</PartnerId>
            <CertificateNumber>{CertificateNumber}</CertificateNumber>
            <AuthorizationCode>{AuthorizationCode}</AuthorizationCode>
            <ThirdPartyId>{ThirdPartyId}</ThirdPartyId>
            <UserName>{UserName}</UserName>
            <Password>AVCTH2024!</Password>
            <FirstName>{FirstName}</FirstName>
            <LastName>{LastName}</LastName>
            <Telephone>{Telephone}</Telephone>
            <CountryCode>{CountryCode}</CountryCode>
            <EmailAddress>{EmailAddress}</EmailAddress>
            <EmailOptIn>true</EmailOptIn>
        </CreateMembershipNG>
    </soap:Body>
</soap:Envelope>""",
        "UpgradeMembership": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <UpgradeMembershipNG xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>mytravel.lifestyle</WsUserName>
            <WsPassword>Ga1N0n1GfNhsDpmlhxag</WsPassword>
            <PartnerId>287</PartnerId>
            <UserAccountToken>{UserAccountToken}</UserAccountToken>
            <CertificateNumber>{CertificateNumber}</CertificateNumber>
            <AuthorizationCode>{AuthorizationCode}</AuthorizationCode>
        </UpgradeMembershipNG>
    </soap:Body>
</soap:Envelope>""",
        "CreateSecondary": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <CreateUserAccount xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>mytravel.lifestyle</WsUserName>
            <WsPassword>Ga1N0n1GfNhsDpmlhxag</WsPassword>
            <PartnerId>287</PartnerId>
            <UserAccountToken>{UserAccountToken}</UserAccountToken>
            <EmailAddress>{EmailAddress}</EmailAddress>
            <UserName>{UserName}</UserName>
            <Password>AVCTH2024!</Password>
            <FirstName>{FirstName}</FirstName>
            <LastName>{LastName}</LastName>
            <Telephone>{Telephone}</Telephone>
            <CountryCode>{CountryCode}</CountryCode>
            <EmailOptIn>true</EmailOptIn>
        </CreateUserAccount>
    </soap:Body>
</soap:Envelope>""",
        "UpdateUserAccount": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <UpdateUserAccount xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>mytravel.lifestyle</WsUserName>
            <WsPassword>Ga1N0n1GfNhsDpmlhxag</WsPassword>
            <PartnerId>287</PartnerId>
            <UserAccountToken>{UserAccountToken}</UserAccountToken>
            <UserAccountXml>
                <![CDATA[
                <UserAccount>
                    <UserAccountToken>{UserAccountToken}</UserAccountToken>
                    <UserName>{UserName}</UserName>
                    <EmailAddress>{EmailAddress}</EmailAddress>
                    <FirstName>{FirstName}</FirstName>
                    <LastName>{LastName}</LastName>
                    <Telephone>{Telephone}</Telephone>
                </UserAccount>]]>
            </UserAccountXml>
        </UpdateUserAccount>
    </soap:Body>
</soap:Envelope>""",
        "UpdateUserPhone": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <UpdateUserAccount xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>mytravel.lifestyle</WsUserName>
            <WsPassword>Ga1N0n1GfNhsDpmlhxag</WsPassword>
            <PartnerId>287</PartnerId>
            <UserAccountToken>{UserAccountToken}</UserAccountToken>
            <UserAccountXml>
                <![CDATA[
                <UserAccount>
                    <UserAccountToken>{UserAccountToken}</UserAccountToken>
                    <UserName>{UserName}</UserName>
                    <Telephone>{Telephone}</Telephone>
                </UserAccount>]]>
            </UserAccountXml>
        </UpdateUserAccount>
    </soap:Body>
</soap:Envelope>""",
        "GetUserAccountToken": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <AuthenticateUserByThirdPartyId2 xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>mytravel.lifestyle</WsUserName>
            <WsPassword>Ga1N0n1GfNhsDpmlhxag</WsPassword>
            <PartnerId>287</PartnerId>
            <ThirdPartyId>{ThirdPartyId}</ThirdPartyId>
        </AuthenticateUserByThirdPartyId2>
    </soap:Body>
</soap:Envelope>""",
        "UpdateThirdPartyId": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <UpdateMembership xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>mytravel.lifestyle</WsUserName>
            <WsPassword>Ga1N0n1GfNhsDpmlhxag</WsPassword>
            <PartnerId>287</PartnerId>
            <UserAccountToken>{UserAccountToken}</UserAccountToken>
            <MembershipUpdateXml>
                <![CDATA[<Membership><ThirdPartyId>{ThirdPartyId}</ThirdPartyId></Membership>]]>
            </MembershipUpdateXml>
        </UpdateMembership>
    </soap:Body>
</soap:Envelope>""",
        "GetMembershipInformation": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <GetMembershipInformation xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>mytravel.lifestyle</WsUserName>
            <WsPassword>Ga1N0n1GfNhsDpmlhxag</WsPassword>
            <PartnerId>287</PartnerId>
            <UserAccountToken>{UserAccountToken}</UserAccountToken>
        </GetMembershipInformation>
    </soap:Body>
</soap:Envelope>"""
    },
    "Travily": {
        "CreateMembership": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <CreateMembershipNG xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>travily.account</WsUserName>
            <WsPassword>Tl^VAuS1-9Ll</WsPassword>
            <PartnerId>290</PartnerId>
            <CertificateNumber>FZRQZQM6</CertificateNumber>
            <AuthorizationCode>HTQ4T2T4</AuthorizationCode>
            <ThirdPartyId>{ThirdPartyId}</ThirdPartyId>
            <UserName>{UserName}</UserName>
            <EmailAddress>{EmailAddress}</EmailAddress>
            <Password>Travily2024!</Password>
            <FirstName>{FirstName}</FirstName>
            <LastName>{LastName}</LastName>
            <Telephone>{Telephone}</Telephone>
            <CountryCode>{CountryCode}</CountryCode>
            <EmailOptIn>true</EmailOptIn>
        </CreateMembershipNG>
    </soap:Body>
</soap:Envelope>""",
        "CreateSecondaryMember": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <CreateUserAccount xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>travily.account</WsUserName>
            <WsPassword>Tl^VAuS1-9Ll</WsPassword>
            <PartnerId>290</PartnerId>
            <UserAccountToken>{UserAccountToken}</UserAccountToken>
            <EmailAddress>{EmailAddress}</EmailAddress>
            <UserName>{UserName}</UserName>
            <Password>Travily2024!</Password>
            <FirstName>{FirstName}</FirstName>
            <LastName>{LastName}</LastName>
            <Telephone>{Telephone}</Telephone>
            <CountryCode>{CountryCode}</CountryCode>
            <EmailOptIn>true</EmailOptIn>
        </CreateUserAccount>
    </soap:Body>
</soap:Envelope>""",
        "UpdateUserAccount": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <UpdateUserAccount xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>travily.account</WsUserName>
            <WsPassword>Tl^VAuS1-9Ll</WsPassword>
            <PartnerId>290</PartnerId>
            <UserAccountToken>{UserAccountToken}</UserAccountToken>
            <UserAccountXml>
                <![CDATA[
                <UserAccount>
                    <UserAccountToken>{UserAccountToken}</UserAccountToken>
                    <UserName>{UserName}</UserName>
                    <EmailAddress>{EmailAddress}</EmailAddress>
                    <FirstName>{FirstName}</FirstName>
                    <LastName>{LastName}</LastName>
                    <Telephone>{Telephone}</Telephone>
                </UserAccount>]]>
            </UserAccountXml>
        </UpdateUserAccount>
    </soap:Body>
</soap:Envelope>""",
        "UpdateUserPhone": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <UpdateUserAccount xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>travily.account</WsUserName>
            <WsPassword>Tl^VAuS1-9Ll</WsPassword>
            <PartnerId>290</PartnerId>
            <UserAccountToken>{UserAccountToken}</UserAccountToken>
            <UserAccountXml>
                <![CDATA[
                <UserAccount>
                    <UserAccountToken>{UserAccountToken}</UserAccountToken>
                    <UserName>{UserName}</UserName>
                    <Telephone>{Telephone}</Telephone>
                </UserAccount>]]>
            </UserAccountXml>
        </UpdateUserAccount>
    </soap:Body>
</soap:Envelope>""",
        "GetUserAccountToken": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <AuthenticateUserByThirdPartyId2 xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>travily.account</WsUserName>
            <WsPassword>Tl^VAuS1-9Ll</WsPassword>
            <PartnerId>290</PartnerId>
            <ThirdPartyId>{ThirdPartyId}</ThirdPartyId>
        </AuthenticateUserByThirdPartyId2>
    </soap:Body>
</soap:Envelope>""",
        "UpdateThirdPartyId": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <UpdateMembership xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>travily.account</WsUserName>
            <WsPassword>Tl^VAuS1-9Ll</WsPassword>
            <PartnerId>290</PartnerId>
            <UserAccountToken>{UserAccountToken}</UserAccountToken>
            <MembershipUpdateXml>
                <![CDATA[<Membership><ThirdPartyId>{ThirdPartyId}</ThirdPartyId></Membership>]]>
            </MembershipUpdateXml>
        </UpdateMembership>
    </soap:Body>
</soap:Envelope>""",
        "GetMembershipInformation": """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <GetMembershipInformation xmlns="http://ourvacationstore.org/MembershipInterface/">
            <WsUserName>travily.account</WsUserName>
            <WsPassword>Tl^VAuS1-9Ll</WsPassword>
            <PartnerId>290</PartnerId>
            <UserAccountToken>{UserAccountToken}</UserAccountToken>
        </GetMembershipInformation>
    </soap:Body>
</soap:Envelope>"""
    }
}

# Validate user input
def validate_inputs(user_inputs, action, uploaded_file):
    if uploaded_file is None:  # Check if a CSV file was uploaded
        missing_inputs = [key for key, value in user_inputs.items() if not value and key != "EmailAddress"]
    else:
        missing_inputs = []

    return missing_inputs

# Function to make SOAP request
def make_soap_request(url, payload):
    try:
        headers = {'Content-Type': 'text/xml'}
        response = requests.post(url, data=payload, headers=headers)
        return response.content
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Function to parse XML response and convert to dictionary
def parse_xml_to_dict(xml_content):
    root = ET.fromstring(xml_content)
    response_dict = {}
    for child in root.iter():
        response_dict[child.tag] = child.text
    return response_dict

# Define Streamlit app
def main():
    st.title("Arrivia API")
    st.subheader("by TC-V1.16.09")
    # Initialize counter
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    # User login
    if 'login' not in st.session_state:
        st.session_state.login = False

    if not st.session_state.login:
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"):
            if username in users and password == users[username]:
                st.session_state.login = True
                st.success("Logged in successfully!")
                st.session_state.counter += 1
                st.sidebar.empty()
                st.sidebar.text(f"Number of Logins: {st.session_state.counter}")
                show_main_app()
            else:
                st.error("Invalid username or password")

    if st.session_state.login:
        show_main_app()

def show_main_app():
    # Initialize an empty DataFrame
    df = pd.DataFrame()

    # Select system
    if 'system' not in st.session_state:
        st.session_state.system = "MT&L"

    # New comment for handle error show on home page
    try:
        system = st.radio("Select system", list(endpoints.keys()),
                      index=list(endpoints.keys()).index(st.session_state.system))
    except Exception as e:
        st.error("An error occurred while selecting the system. Please try again.")
        return

    # Select action
    available_actions = list(endpoints[system].keys())
    if 'action' not in st.session_state or st.session_state.action not in available_actions:
        st.session_state.action = available_actions[0]

    action = st.selectbox("Select action", available_actions,
                          index=available_actions.index(st.session_state.action))

    st.session_state.system = system
    st.session_state.action = action

    # Show corresponding payload template
    payload_template = payloads[st.session_state.system][st.session_state.action]
    st.text("Payload:")
    st.code(payload_template)

    # Dropdown for selecting membership type if action is "UpgradeMembership"
    if st.session_state.action == "UpgradeMembership":
        selected_membership_type = st.selectbox("Select Membership Type", list(membership_types.keys()))
        cert_text = st.text_input("Certificate Number", membership_types[selected_membership_type]["Cert"])
        auth_text = st.text_input("Authorization Code", membership_types[selected_membership_type]["Auth"])

    # Initialize user_inputs dictionary
    user_inputs = {}

    # File upload
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    if uploaded_file is not None:
        try:
            # Read the CSV file, specifying the data types for ThirdPartyId as str to prevent automatic conversion to float
            df = pd.read_csv(uploaded_file, dtype={'ThirdPartyId': 'str'})

            # ensure ThirdPartyId is treated as a string and remove any commas or periods
            df["ThirdPartyId"] = df["ThirdPartyId"].str.replace(".", "").astype(str)
            st.write("### Uploaded CSV data")
            st.write(df)

            # Extract the necessary input data from the CSV file based on the selected action
            if st.session_state.action == "CreateMembership":
                user_inputs["CertificateNumber"] = df["CertificateNumber"].tolist()
                user_inputs["AuthorizationCode"] = df["AuthorizationCode"].tolist()
                user_inputs["ThirdPartyId"] = df["ThirdPartyId"].tolist()
                user_inputs["UserName"] = df["UserName"].tolist()
                user_inputs["FirstName"] = df["FirstName"].tolist()
                user_inputs["LastName"] = df["LastName"].tolist()
                user_inputs["Telephone"] = df["Telephone"].tolist()
                user_inputs["CountryCode"] = df["CountryCode"].tolist()
                user_inputs["EmailAddress"] = df["EmailAddress"].tolist()
        except Exception as e:
            st.error("An error occurred while reading the CSV file. Please check the file format and try again.")
            return

    # Get user input for variables in the payload
    counter = 1
    for line in payload_template.split("\n"):
        if "{" in line and "}" in line:
            variable_name = line.split("{")[1].split("}")[0]
            unique_key = f"{st.session_state.system}_{st.session_state.action}_{variable_name}_{counter}"
            # Check if the variable is not provided in the CSV
            if variable_name not in user_inputs:
                user_input = st.text_input(variable_name, key=unique_key)
                user_inputs[variable_name] = user_input
            counter += 1

    # Submit button
    if st.button("Submit"):
        # Record the start time
        start_time = time.time()

        # Check for missing inputs
        missing_inputs = validate_inputs(user_inputs, st.session_state.action, uploaded_file)
        if missing_inputs:
            st.error(f"Missing input(s): {', '.join(missing_inputs)}")
        else:
            # Initialize a variable to store all responses
            all_responses = []

            # Initialize progress bar
            progress_bar = st.progress(0)

            # Handle manual input case
            if uploaded_file is None:
                # Construct the payload using manual input
                payload = payload_template.format(**user_inputs)

                # Make the SOAP request
                url = endpoints[st.session_state.system][st.session_state.action]
                response_content = make_soap_request(url, payload)

                # Parse and append the response to all_responses
                if response_content is not None:
                    response_dict = parse_xml_to_dict(response_content)
                    all_responses.append(response_dict)

            # Handle CSV file upload case
            else:
                # Get total number of rows for progress calculation
                total_rows = len(df)

                # Iterate through each row in the DataFrame
                for index, row in df.iterrows():
                    # Construct user_inputs dictionary for the current row
                    user_inputs_row = {}
                    for column in df.columns:
                        user_inputs_row[column] = row[column]

                    # Construct the payload for the current row
                    payload = payload_template.format(**user_inputs_row)

                    # Make the SOAP request for the current row
                    url = endpoints[st.session_state.system][st.session_state.action]
                    response_content = make_soap_request(url, payload)

                    # Parse and append the response to all_responses
                    if response_content is not None:
                        response_dict = parse_xml_to_dict(response_content)
                        all_responses.append(response_dict)

                    # Update progress bar
                    progress_bar.progress((index + 1) / total_rows)

            # Close progress bar
            progress_bar.empty()

            # Record the end time
            end_time = time.time()

            # Calculate the elapsed time
            elapsed_time = end_time - start_time
            minutes, seconds = divmod(elapsed_time, 60)
            st.write(f"Total processing time: {int(minutes)} minutes and {seconds:.2f} seconds")

            # Display all responses in a table
            if all_responses:
                response_df = pd.DataFrame(all_responses)
                st.write("### All Responses")
                st.write(response_df)

if __name__ == "__main__":
    main()