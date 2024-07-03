import allure
from demo_aqa_2gis_tests.pages.ui.bookmarkers_page import bookmarkers_page
from tests.ui.test_log_in import test_checking_account_log_in


@allure.suite('Добавление в избранное')
@allure.title('Проверка добавления в избранное')
def test_adding_to_bookmarks(test_checking_account_log_in):
    bookmarkers_page.adding_to_bookmarks()
    bookmarkers_page.checking_that_we_are_logging_in()
    bookmarkers_page.deleting_from_bookmarks()
