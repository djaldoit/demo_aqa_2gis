import time
import allure
from pages.avatar_page import AvatarPage
from tests.test_log_in import test_checking_account_log_in


@allure.suite('Смена аватара')
@allure.title('Проверка добавления аватара')
def test_avatar_adding():
    test_checking_account_log_in()
    page = AvatarPage()
    time.sleep(3)
    page.adding_an_avatar()
    page.adding_avatar()
    page.upload_avatar()
    page.save_avatar()


