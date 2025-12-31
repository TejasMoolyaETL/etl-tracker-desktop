import requests
from config.config import BASE_URL

def login(email, password):
    payload = {
        "email": email,
        "password": password
    }

    try:
        res = requests.post(f"{BASE_URL}/auth/login", json=payload)

        if res.status_code != 200:
            return {"status": "FAILURE", "msg": "Invalid credentials"}

        return res.json()

    except Exception:
        return {"status": "FAILURE", "msg": "Server not reachable"}
