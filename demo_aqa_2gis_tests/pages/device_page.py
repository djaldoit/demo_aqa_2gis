import allure
from selene import browser, be, have

from demo_aqa_2gis_tests.test_data.data import Urls


class DevicePage:

    @allure.step('Открытие главной страницы')
    def browser_open(self):
        browser.open(Urls.main_url())
        return self

    @allure.step('Клик по кнопке Меню в лендинге"')
    def click_menu(self):
        browser.element('//button[@class="_1xj5mhp"]').with_(timeout=10).should(be.visible).click()
        return self

    @allure.step('Клик по ссылке "Android"')
    def click_on_android(self):
        browser.element('//a[text()="Android"]').should(be.visible).click()
        return self

    @allure.step('Клик по ссылке "iOS"')
    def click_on_ios(self):
        browser.element('//a[text()="iOS"]').should(be.visible).click()
        return self

    @allure.step('Клик по ссылке "ПК-версия"')
    def click_on_pc(self):
        browser.element('//a[text()="ПК-версия"]').should(be.visible).click()
        return self

    @allure.step('Переключение на второй вкладку и получение iOS URL')
    def should_ios_page(self):
        browser.switch_to_tab(1)
        browser.should(have.url(Urls.ios_version()))
        return self

    @allure.step('Переключение на второй вкладку и получение Android URL')
    def should_android_page(self):
        browser.switch_to_tab(1)
        browser.should(have.url(Urls.android_version()))
        return self

    @allure.step('Переключение на второй вкладку и получение ПК URL')
    def should_pc_page(self):
        browser.switch_to_tab(1)
        browser.should(have.url(Urls.pc_version()))
        return self


device_page = DevicePage()