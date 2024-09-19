# soap_client.py
import requests
import xml.etree.ElementTree as ET
import streamlit as st

class SOAPClient:
    def __init__(self, ws_user_name, ws_password, partner_id):
        self.ws_user_name = ws_user_name
        self.ws_password = ws_password
        self.partner_id = partner_id

    def send_request(self, url, payload):
        headers = {'Content-Type': 'text/xml'}
        try:
            response = requests.post(url, data=payload, headers=headers)
            return response.content
        except Exception as e:
            st.error(f"SOAP request error: {e}")
            return None

    def format_payload(self, template, data):
        return template.format(**data)

    def parse_response(self, response):
        root = ET.fromstring(response)
        parsed_data = {child.tag: child.text for child in root.iter()}
        return parsed_data
