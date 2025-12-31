import requests
from session.session_manager import SessionManager
from models.organization import Organization


BASE_URL = "http://localhost:8080/api"


def get_all_organizations():
    token = SessionManager.get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{BASE_URL}/organizations/getAllOrg",
        headers=headers,
        timeout=10
    )

    if response.status_code != 200:
        raise Exception("Failed to fetch organizations")

    data = response.json()

    organizations = []
    for item in data:
        organizations.append(
            Organization(
                org_code=item.get("orgCode"),
                org_name=item.get("orgName")
            )
        )

    return organizations
