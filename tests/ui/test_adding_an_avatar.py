import allure
from demo_aqa_2gis_tests.pages.ui import avatar_page
from tests.ui.test_log_in import test_checking_account_log_in


@allure.suite('Смена аватара')
@allure.title('Проверка добавления аватара')
def test_avatar_adding(test_checking_account_log_in):
    avatar_page.adding_an_avatar()
    avatar_page.adding_avatar()
    avatar_page.upload_avatar()
    avatar_page.save_avatar()
