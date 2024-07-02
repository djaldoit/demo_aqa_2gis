import allure
from selene import browser, have, be
from selene.support.conditions.be import visible

from data import Urls


class RoutePage:
    @allure.step('Open main page')
    def browser_open(self):
        browser.open(Urls.main_url())
        return self

    @allure.step('Searching for route')
    def searching_for_route(self):
        browser.element('//input[@placeholder="Поиск в 2ГИС"]').type('Московский Кремль').press_enter()
        browser.element('//span[@class="_1al0wlf"]').click()

    @allure.step('Finding route')
    def finding_route(self):
        browser.element('//span[text()="Проехать"]').assure(visible, timeout=15).click()
        return self

    @allure.step('Checking route')
    def checking_route(self):
        browser.element('//input[@placeholder="Откуда"]').send_keys("Санкт-Петербург")
        browser.element('//div[text()="Санкт-Петербург"]').click()
        return self

    @allure.step('Checking distance')
    def checking_distance(self):
        browser.element('//div[@class="_sgs1pz"]').should(be.visible)
        return self