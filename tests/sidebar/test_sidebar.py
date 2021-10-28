from selenium.common.exceptions import NoSuchElementException
import pytest

sidebar_elements = [
    'com.ajaxsystems:id/menuTitle',
    'com.ajaxsystems:id/addHub',
    'com.ajaxsystems:id/settings',
    'com.ajaxsystems:id/help',
    'com.ajaxsystems:id/logs',
    'com.ajaxsystems:id/agreementText'
]


@pytest.mark.parametrize('element', sidebar_elements)
def test_sidebar_element(sidebar_fixture, element):
    # Try to find element in sidebar
    try:
        main_page = sidebar_fixture
        main_page.find_element(element)
    except NoSuchElementException:
        assert False
    assert True
