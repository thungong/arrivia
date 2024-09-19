# config.py
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