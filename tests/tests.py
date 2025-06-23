import time

from models.mod_user import UserModel

class TestAddUser:
    def test_valid(self, register_admin, add_login_page):

        user_data = UserModel().random_user()
        add_login_page.add_user_info(data=user_data)
        result_user = add_login_page.get_add_result()
        assert "Пользователь успешно добавлен!" in result_user, "Ошибка добавления пользователя"

    def test_invalid_1(self, register_admin, add_login_page):

        user_data = UserModel().random_user()
        user_data["name"] = None
        add_login_page.add_user_info(data=user_data)
        result_user = add_login_page.get_add_result()
        add_login_page.clean_form()
        time.sleep(3)
        assert "Поле обязательно" in result_user, "Ошибочное добавление пользователя"

    def test_invalid_2(self, register_admin, add_login_page):

        user_data = UserModel().random_user()
        user_data["age"] = None
        add_login_page.add_user_info(data=user_data)
        result_user = add_login_page.get_add_result()
        add_login_page.clean_form()
        time.sleep(3)
        assert "Поле обязательно" in result_user, "Ошибочное добавление пользователя"

