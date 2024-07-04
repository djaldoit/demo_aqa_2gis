import os
import random
import allure
from selene import browser, be
from demo_aqa_2gis_tests.test_data.data import Urls


class AvatarPage:
    @allure.step('Open main page')
    def browser_open(self):
        browser.open(Urls.main_url())
        return self

    @allure.step('Click account')
    def adding_an_avatar(self):
        browser.element('//div[@class="_n5j5w"]').should(be.visible).click()
        return self

    @allure.step('Click settings')
    def adding_avatar(self):
        browser.element('(//div[@class="_1x4n3b4"])[1]').should(be.visible).click()
        return self

    @allure.step('Upload avatar')
    def upload_avatar(self):
        browser.element('//input[@id="avatar-uploader"]').send_keys(os.path.abspath(
            os.path.abspath(os.path.join(os.getcwd(), f'test_data/pictures/{random.choice(
                ["avatar.jpg", "avatar2.jpg"])}'))))
        return self

    @allure.step('Save settings')
    def save_avatar(self):
        browser.element('//button[text()="Сохранить"]').should(be.visible).click()
        return self


avatar_page = AvatarPage()
