from selenium.webdriver.common.by import By

class UserLocators:
    NAME = (By.ID, "name")
    AGE = (By.ID, "age")
    GENDER = (By.ID, "gender")
    DATE = (By.ID, "date_birthday")
    STATUS = (By.ID, "isActive")
    SAVE_BUTTON = (By.ID, 'add-btn')
    MESSAGE = (By.XPATH, '//div[@class="alert alert-success"]')
    ERROR_AGE = (By.ID, 'ageError')
    ERROR_NAME = (By.ID, 'nameError')