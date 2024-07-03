import allure
from selene import browser, be


class BookmarkersPage:

    @allure.step('Поиск места для избранного')
    def adding_to_bookmarks(self):
        browser.element('//input[@placeholder="Поиск в 2ГИС"]').type('Московский Кремль').press_enter()
        browser.element('//span[text()="Сохранить"]').should(be.visible).click()
        return self

    @allure.step('Возвращаемся до избранного')
    def checking_that_we_are_logging_in(self):
        browser.element('(//div[@class="_rfz2ij"])[1]').should(be.visible).click().click()
        return self

    @allure.step('Удаление из избранного')
    def deleting_from_bookmarks(self):
        # Удаление из избранного
        browser.element('//a[@title="Избранное"]').should(be.visible).click()
        browser.element('(//div[@class="_699xer"])[1]').click()
        browser.element('//button[text()="Московский Кремль"]').should(be.visible).click()
        browser.element('//span[text()="Сохранено"]').should(be.visible).click()
        browser.element('(//div[@class="_mkajyk"])[1]').click()
        browser.element('//button[text()="Сохранить"]').click()
        browser.element('//span[text()="Сохранить"]').should(be.visible)


bookmarkers_page = BookmarkersPage()
