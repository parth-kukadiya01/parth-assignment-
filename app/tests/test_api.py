import requests

BASE_URL = "http://localhost:8000"

def test_root():
    print("Testing root endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Root endpoint response: {response.json()}")
    except Exception as e:
        print(f"Root endpoint failed: {e}")

def test_register_admin():
    print("Registering admin user...")
    admin_data = {"username": "admin", "password": "admin123", "role": "admin"}
    try:
        response = requests.post(f"{BASE_URL}/register", json=admin_data)
        if response.status_code == 201:
            print(f"Admin registered: {response.json()}")
        else:
            print(f"Admin registration response: {response.status_code} {response.text}")
    except Exception as e:
        print(f"Admin registration failed: {e}")

def test_login_admin():
    print("Logging in admin user...")
    login_data = {"username": "admin", "password": "admin123"}
    try:
        response = requests.post(f"{BASE_URL}/login", json=login_data)
        if response.status_code == 200:
            token = response.json()["access_token"]
            print(f"Admin login successful, token: {token}")
            return token
        else:
            print(f"Admin login failed: {response.status_code} {response.text}")
    except Exception as e:
        print(f"Admin login failed: {e}")
    return None

def test_get_me(token):
    print("Testing /me endpoint...")
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{BASE_URL}/me", headers=headers)
        print(f"/me endpoint: {response.json()}")
    except Exception as e:
        print(f"/me endpoint failed: {e}")

def run_all_tests():
    print("Running all tests...\n")
    test_root()
    test_register_admin()
    token = test_login_admin()
    if token:
        test_get_me(token)
    print("\nAll tests finished.")

if __name__ == "__main__":
    run_all_tests()