import time
import pytest
from pages.bookmarkers_page import BookmarkersPage


@pytest.mark.order(2)
def test_adding_to_bookmarks():
    page = BookmarkersPage()
    time.sleep(5)
    page.adding_to_bookmarks()
    page.checking_that_we_are_logging_in()
    page.deleting_from_bookmarks()

