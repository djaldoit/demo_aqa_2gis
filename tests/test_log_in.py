import allure
import pytest
from pages.log_in_page import LogInPage


@pytest.mark.order(1)
@allure.suite('Вход в аккаунт')
@allure.title('Проверка входа в аккаунт')
def test_checking_account_log_in():
    page = LogInPage()
    page.browser_open()
    page.click_on_log_in()
    page.click_on_email_sign_in()
    page.login_in()
    page.confirm_that_we_are_logged_in()
    page.checking_that_we_are_logging_in()

