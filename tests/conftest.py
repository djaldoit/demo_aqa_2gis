import os

import pytest
from selenium import webdriver
from dotenv import load_dotenv
from selene import browser
from selenium.webdriver.chrome.options import Options

from demo_aqa_2gis_tests.pages.log_in_page import login_page
from demo_aqa_2gis_tests.utils import attachments
from tests.test_log_in import test_checking_account_log_in

DEFAULT_BROWSER_VERSION = "122.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version', default='122.0')


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture
def account_login():
    login_page.browser_open()
    login_page.click_on_log_in()
    login_page.click_on_email_sign_in()
    login_page.login_in()
    login_page.confirm_that_we_are_logged_in()
    login_page.checking_that_we_are_logging_in()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attachments.add_html(browser)
    attachments.add_screenshot(browser)
    attachments.add_logs(browser)
    attachments.add_video(browser)
    browser.quit()
