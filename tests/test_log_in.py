import allure
from demo_aqa_2gis_tests.pages.log_in_page import login_page


@allure.suite('Вход в аккаунт')
@allure.title('Проверка входа в аккаунт')
def test_checking_account_log_in():
    login_page.browser_open()
    login_page.click_on_log_in()
    login_page.click_on_email_sign_in()
    login_page.login_in()
    login_page.confirm_that_we_are_logged_in()
    login_page.checking_that_we_are_logging_in()
