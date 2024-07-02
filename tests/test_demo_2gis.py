import time

import allure

from pages.avatar_page import AvatarPage
from pages.bookmarkers_page import BookmarkersPage
from pages.log_in_page import LogInPage
from pages.route_page import RoutePage


class TestDemo2Gis:
    @allure.title('Checking account log in')
    def test_checking_account_log_in(self):
        log_in_page = LogInPage()
        log_in_page.browser_open()
        log_in_page.click_on_log_in()
        log_in_page.click_on_email_sign_in()
        log_in_page.login_in()
        log_in_page.confirm_that_we_are_logged_in()
        log_in_page.checking_that_we_are_logging_in()
        time.sleep(3)

    @allure.title('Adding to bookmarks')
    def test_adding_to_bookmarks(self):
        bookmarks_page = BookmarkersPage()
        time.sleep(3)
        bookmarks_page.adding_to_bookmarks()
        bookmarks_page.checking_that_we_are_logging_in()
        bookmarks_page.deleting_from_bookmarks()

    @allure.title('Adding an avatar')
    def test_avatar_adding(self):
        avatar_page = AvatarPage()
        time.sleep(3)
        avatar_page.adding_an_avatar()
        avatar_page.adding_avatar()
        avatar_page.upload_avatar()
        avatar_page.save_avatar()

    @allure.title('Checking route')
    def test_route(self):
        route_page = RoutePage()
        time.sleep(3)
        route_page.searching_for_route()
        route_page.finding_route()
        route_page.checking_route()
        route_page.checking_distance()