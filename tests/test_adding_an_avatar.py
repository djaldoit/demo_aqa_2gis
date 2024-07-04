import allure
from demo_aqa_2gis_tests.pages.avatar_page import avatar_page
from tests.conftest import account_login


@allure.suite('Смена аватара')
@allure.title('Проверка добавления аватара')
def test_avatar_adding(account_login):
    avatar_page.adding_an_avatar()
    avatar_page.adding_avatar()
    avatar_page.upload_avatar()
    avatar_page.save_avatar()
