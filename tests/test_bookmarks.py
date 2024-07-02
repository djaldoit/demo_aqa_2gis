import time
import allure
from pages.bookmarkers_page import BookmarkersPage
from tests.test_log_in import test_checking_account_log_in


@allure.suite('Добавление в избранное')
@allure.title('Проверка добавления в избранное')
def test_adding_to_bookmarks():
    test_checking_account_log_in()
    page = BookmarkersPage()
    time.sleep(3)
    page.adding_to_bookmarks()
    page.checking_that_we_are_logging_in()
    page.deleting_from_bookmarks()

