import allure
from demo_aqa_2gis_tests.pages.ui.route_page import route_page


@allure.suite('Построение маршрута')
@allure.title('Проверка построения маршрута')
def test_route():
    route_page.browser_open()
    route_page.searching_for_route()
    route_page.finding_route()
    route_page.checking_route()
    route_page.checking_distance()
