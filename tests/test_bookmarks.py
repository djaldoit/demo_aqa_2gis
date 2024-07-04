import allure
from demo_aqa_2gis_tests.pages.bookmarkers_page import bookmarkers_page
from tests.conftest import account_login


@allure.suite('Добавление в избранное')
@allure.title('Проверка добавления в избранное')
def test_adding_to_bookmarks(account_login):
    bookmarkers_page.adding_to_bookmarks()
    bookmarkers_page.checking_that_we_are_logging_in()
    bookmarkers_page.deleting_from_bookmarks()
