import time
import pytest
from pages.avatar_page import AvatarPage


@pytest.mark.order(3)
def test_avatar_adding():
    page = AvatarPage()
    time.sleep(5)
    page.adding_an_avatar()
    page.adding_avatar()
    page.upload_avatar()
    page.save_avatar()


