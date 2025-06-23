from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _find_element(self, locator, wait_time=10):
        '''
        Поиск элемента на веб-странице, с ожиданием загрузки (внутренний метод)
        '''
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"ErrLoc: can't find element by locator {locator}",
        )
        return element

    def _find_element_for_add_form(self, locator_success, locator_error_name, locator_error_age, wait_time=10):
        '''
        Поиск элемента на веб-странице, с ожиданием загрузки (внутренний метод)
        '''
        element = WebDriverWait(self.driver, wait_time).until(
            EC.any_of(
                EC.visibility_of_element_located(locator_success),
                EC.visibility_of_element_located(locator_error_name),
                EC.visibility_of_element_located(locator_error_age),
            )
        )
        return element

    def click(self, locator, wait_time=10):
        '''
        Наажатие кнопки
         '''
        element = self._find_element(locator, wait_time)
        element.click()

    def fill(self, value: str, locator, wait_time=60):
        '''
        fill = send_keys - т.е. заполнение текстового поля
        '''
        element = self._find_element(locator, wait_time)
        if value:
            element.send_keys(value)

    def text(self, locator_success, locator_error_name, locator_error_age, wait_time=20) -> str:
        '''

        :param locator_error_age:
        :param locator_error_name:
        :param locator_success:
        :param wait_time: аналогичен (By.ID, 'username')
        :return: текст ошибки (для нашего приложения - текст в поле вывода)
        '''

        element = self._find_element_for_add_form(locator_success, locator_error_name, locator_error_age, wait_time)
        return element.text

    def url_check(self, wait_time=10)-> bool:
        '''
        :param wait_time:
        :return:
        '''
        element = WebDriverWait(self.driver, wait_time).until(EC.url_contains("/users-page"))
        if element:
            return True
        else:
            return False

    def cleaner(self, locators, wait_time=10):
        self._find_element(locators["0"], wait_time).clear()
        self._find_element(locators["1"], wait_time).clear()
        self._find_element(locators["2"], wait_time).clear()
        self._find_element(locators["3"], wait_time).clear()
        checkbox = self._find_element(locators["4"], wait_time)
        if checkbox.is_selected():
            checkbox.clear()