import allure
import pytest
from demo_aqa_2gis_tests.pages.device_page import device_page


@pytest.mark.parametrize('device', ['Android', 'iOS', 'ПК-версия'])
@allure.title('Проверка сайта приложений для устройств')
def test_os_app(device):
    device_page.browser_open()
    device_page.click_on_the_menu()
    if device == 'Android':
        device_page.click_on_android()
        device_page.should_android_page()
    elif device == 'iOS':
        device_page.click_on_ios()
        device_page.should_ios_page()
    elif device == 'ПК-версия':
        device_page.click_on_pc()
        device_page.should_pc_page()