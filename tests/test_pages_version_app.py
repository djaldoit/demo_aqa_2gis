import allure
import pytest
from demo_aqa_2gis_tests.pages.device_page import device_page


@pytest.mark.parametrize('device', ['android', 'ios', 'pc'])
@allure.title('Проверка сайта приложений для Android, iOS и ПК устройств')
def test_device_version(device):
    device_page.browser_open()
    device_page.click_on_the_menu()
    if device == 'android':
        device_page.click_on_android()
        device_page.should_android_page()
    elif device == 'ios':
        device_page.click_on_ios()
        device_page.should_ios_page()
    elif device == 'pc':
        device_page.click_on_pc()
        device_page.should_pc_page()