import requests
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://158.160.87.146:5000/"
fake = Faker()

class TestRegisterNewUser:
    def test_register_admin(self):
        """
        1. Try to register admin
        2. Check status code is 200
        3. Check response
        """
        driver = webdriver.Chrome()
        driver.get(url=f"{URL}/register")

        body = {"login": fake.email(), "password": "Pass"}
        response = requests.post(url=f"{URL}/register", json=body)

        # driver.find_element(By.NAME, "login").send_keys("admin10")
        # driver.find_element(By.NAME, "password").send_keys("<PASS>")
        driver.find_element(By.XPATH, "/html/body/div/form/button").click()
        driver.implicitly_wait(3)

        assert response.status_code == 200, f"Check register request, status code is {response.status_code}"
        assert response.json()['message'] is not None
        driver.quit()


    def test_register_new_user(self):
        """
        1. Try to register new user
        2. Check status code is 200
        3. Check response
        """
        body = {"login": fake.email(), "password": "Password"}
        response = requests.post(url=f"{URL}/user", json=body)
        assert response.status_code == 200, f"Check register request, status code is {response.status_code}"
        assert response.json()['message'] is not None
#        assert response.json()['uuid'] is not None
#        assert response.json()['message'] == "User created successfully."
#        assert isinstance(response.json()['message'], str)
#        assert isinstance(response.json()['uuid'], int)

    def test_register_new_user_with_empty_username(self):
        """
        1. Try to register new user with empty username
        2. Check status code is 400
        3. Check response
        """
        body = {"username": None, "password": "Password"}
        response = requests.post(url=f"{URL}/user", json=body)
        assert response.status_code == 400, f"Check register request, status code is {response.status_code}"
        assert response.json()['message'] == "Username and password are required fields"

    def test_register_new_user_with_empty_password(self):
        """
        1. Try to register new user with empty password
        2. Check status code is 400
        3. Check response
        """
        body = {"username": fake.email(), "password": None}
        response = requests.post(url=f"{URL}/user", json=body)
        assert response.status_code == 400, f"Check register request, status code is {response.status_code}"
        assert response.json()['message'] == "Username and password are required fields"