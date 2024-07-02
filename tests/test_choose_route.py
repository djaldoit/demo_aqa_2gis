import time
import allure
from pages.route_page import RoutePage
from tests.test_log_in import test_checking_account_log_in


@allure.suite('Построение маршрута')
@allure.title('Проверка построения маршрута')
def test_route():
    test_checking_account_log_in()
    page = RoutePage()
    time.sleep(3)
    page.searching_for_route()
    page.finding_route()
    page.checking_route()
    page.checking_distance()



