import allure
from selene import browser, be

from data import Urls


class BookmarkersPage:
    @allure.step('Open main page')
    def browser_open(self):
        browser.open(Urls.main_url())
        return self

    @allure.step('Searching for bookmarks')
    def adding_to_bookmarks(self):
        browser.element('//input[@placeholder="Поиск в 2ГИС"]').with_(timeout=15).type('Московский Кремль').press_enter()
        browser.element('//span[@class="_1al0wlf"]').with_(timeout=15).click()
        browser.element('//span[text()="Сохранить"]').with_(timeout=15).should(be.visible).click()
        return self

    @allure.step('Checking added to bookmarks')
    def checking_that_we_are_logging_in(self):
        browser.element('//span[text()="Добавлено в «Избранное»"]').with_(timeout=15).should(be.visible)
        browser.element('(//div[@class="_rfz2ij"])[1]').with_(timeout=15).should(be.visible).click().click()
        return self

    @allure.step('Deleting from bookmarks')
    def deleting_from_bookmarks(self):
        # Удаление из избранного
        browser.element('//a[@title="Избранное"]').with_(timeout=15).should(be.visible).click()
        browser.element('(//div[@class="_699xer"])[1]').with_(timeout=15).click()
        browser.element('//button[text()="Московский Кремль"]').with_(timeout=15).should(be.visible).click()
        browser.element('//span[text()="Сохранено"]').with_(timeout=15).should(be.visible).click()
        browser.element('(//div[@class="_mkajyk"])[1]').with_(timeout=15).click()
        browser.element('//button[text()="Сохранить"]').with_(timeout=15).click()
        browser.element('//span[text()="Сохранить"]').with_(timeout=15).should(be.visible)