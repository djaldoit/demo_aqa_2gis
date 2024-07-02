import allure
from selene import be, browser

from data import User, Urls


class LogInPage:
    @allure.step('Open main page')
    def browser_open(self):
        browser.open(Urls.main_url())
        return self

    @allure.step('Click on Log in')
    def click_on_log_in(self):
        browser.element('//div[@class="_h3r6b0"]').with_(timeout=15).click()
        return self

    @allure.step('Click on Email sign in')
    def click_on_email_sign_in(self):
        browser.element('//div[text()="Войти по E-mail"]').with_(timeout=15).should(be.visible).click()
        return self

    @allure.step('Login in')
    def login_in(self):
        browser.element('//input[@type="email"]').with_(timeout=15).should(be.blank).type(User.user_data()['email'])
        browser.element('//input[@type="password"]').with_(timeout=15).should(be.blank).type(User.user_data()['password'])
        browser.element('//button[@type="submit"]').with_(timeout=15).click()
        return self

    @allure.step('Confirm that we are logged in')
    def confirm_that_we_are_logged_in(self):
        browser.element('//button[text()="Подтверждаю"]').with_(timeout=15).should(be.visible).double_click()
        return self

    @allure.step('Checking that we are logging in')
    def checking_that_we_are_logging_in(self):
        browser.element('//div[@class="_1dk5lq4"]').with_(timeout=15).should(be.visible)
        return self