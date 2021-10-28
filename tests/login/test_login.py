from selenium.common.exceptions import NoSuchElementException
from framework import LoginPage
import pytest

correct_data = [('qa.ajax.app.automation@gmail.com', 'qa_automation_password')]

wrong_data = [
    ('wrong_mail', 'wrong_pass'),
    ('', ''),
    ('wrong_mail', ''),
    ('', 'wrong_pass')
]


@pytest.mark.parametrize('login, password', correct_data)
def test_user_login(user_login_fixture, login, password):
    # Create login page and assign dict element_is
    login_page = user_login_fixture.create_page(LoginPage)
    # Login in app
    login_page.log_in(login, password)

    # Try to find elements which are located on the main page
    try:
        login_page.find_element('com.ajaxsystems:id/pager')
        assert True
    except NoSuchElementException:
        try:
            login_page.find_element('com.ajaxsystems:id/loading')
        except NoSuchElementException:
            assert False


@pytest.mark.parametrize('wrong_login, wrong_password', wrong_data)
def test_negative_user_login(user_login_fixture, wrong_login, wrong_password):
    # Create login page and assign dict element_is
    login_page = user_login_fixture.create_page(LoginPage)
    # Login in app
    login_page.log_in(wrong_login, wrong_password)

    # Try to find elements which are located on the main page
    try:
        login_page.find_element('com.ajaxsystems:id/pager')
        assert False
    except NoSuchElementException:
        try:
            login_page.find_element('com.ajaxsystems:id/loading')
        except NoSuchElementException:
            assert True
