import allure
from selene import browser, have, be

from data import Urls


class RoutePage:
    @allure.step('Open main page')
    def browser_open(self):
        browser.open(Urls.main_url())
        return self

    @allure.step('Searching for route')
    def searching_for_route(self):
        browser.element('//input[@placeholder="Поиск в 2ГИС"]').with_(timeout=15).click().press_enter()
        browser.element('//span[@class="_1al0wlf"]').with_(timeout=15).click()

    @allure.step('Finding route')
    def finding_route(self):
        browser.element('//span[text()="Проехать"]').with_(timeout=15).click()
        return self

    @allure.step('Checking route')
    def checking_route(self):
        browser.element('//input[@placeholder="Откуда"]').with_(timeout=15).send_keys("Санкт-Петербург")
        browser.element('//div[text()="Санкт-Петербург"]').with_(timeout=15).click()
        return self

    @allure.step('Checking distance')
    def checking_distance(self):
        browser.element('//div[@class="_sgs1pz"]').with_(timeout=15).should(be.visible)
        return self