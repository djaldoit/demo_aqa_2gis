import allure
from selene import be, browser

from data import User, Urls


class LogInPage:

    @allure.step('Открытие главной страницы')
    def browser_open(self):
        browser.open(Urls.main_url())
        return self

    @allure.step('Клик по кнопке входа')
    def click_on_log_in(self):
        browser.element('//div[@class="_h3r6b0"]').click()
        return self

    @allure.step('Клик по кнопке "Войти по E-mail"')
    def click_on_email_sign_in(self):
        browser.element('//div[text()="Войти по E-mail"]').should(be.visible).click()
        return self

    @allure.step('Заполнение полей логина и пароля')
    def login_in(self):
        browser.element('//input[@type="email"]').should(be.blank).type(User.user_data()['email'])
        browser.element('//input[@type="password"]').should(be.blank).type(User.user_data()['password'])
        browser.element('//button[@type="submit"]').click()
        return self

    @allure.step('Потверждение входа')
    def confirm_that_we_are_logged_in(self):
        browser.element('//button[text()="Подтверждаю"]').should(be.visible).double_click()
        return self

    @allure.step('Проверка что мы вошли в аккаунт')
    def checking_that_we_are_logging_in(self):
        browser.element('//div[@class="_1dk5lq4"]').should(be.visible)
        return self