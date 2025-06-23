from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN = (By.XPATH, '//input[@name="login"]')
    PASSWORD = (By.XPATH, '//input[@type="password"]')
    LOGIN_BUTTON = (By.ID, 'add-btn')
    TO_ADD_USER = (By.XPATH, '//a[@href="/add-user"]')