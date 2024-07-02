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
        browser.element('//input[@placeholder="Поиск в 2ГИС"]').type('Московский Кремль').press_enter()
        browser.element('//span[text()="Сохранить"]').should(be.visible).click()
        return self

    @allure.step('Сhecking favorites')
    def checking_that_we_are_logging_in(self):
        browser.element('(//div[@class="_rfz2ij"])[1]').should(be.visible).click().click()
        return self

    @allure.step('Deleting from bookmarks')
    def deleting_from_bookmarks(self):
        # Удаление из избранного
        browser.element('//a[@title="Избранное"]').should(be.visible).click()
        browser.element('(//div[@class="_699xer"])[1]').click()
        browser.element('//button[text()="Московский Кремль"]').should(be.visible).click()
        browser.element('//span[text()="Сохранено"]').should(be.visible).click()
        browser.element('(//div[@class="_mkajyk"])[1]').click()
        browser.element('//button[text()="Сохранить"]').click()
        browser.element('//span[text()="Сохранить"]').should(be.visible)