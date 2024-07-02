import time
import pytest
from pages.route_page import RoutePage


@pytest.mark.order(4)
def test_route():
    page = RoutePage()
    time.sleep(5)
    page.searching_for_route()
    page.finding_route()
    page.checking_route()
    page.checking_distance()



