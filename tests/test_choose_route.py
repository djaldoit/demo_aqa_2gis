import time
import pytest
from pages.route_page import RoutePage
from tests.test_log_in import test_checking_account_log_in


@pytest.mark.order(4)
def test_route():
    test_checking_account_log_in()
    page = RoutePage()
    time.sleep(5)
    page.searching_for_route()
    page.finding_route()
    page.checking_route()
    page.checking_distance()



