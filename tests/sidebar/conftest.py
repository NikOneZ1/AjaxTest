from framework import LoginPage, MainPage
import pytest
import time


@pytest.fixture(scope='module')
def sidebar_fixture(page_manager):
    # Login in app
    login_page = page_manager.create_page(LoginPage)
    login_page.log_in('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    main_page = page_manager.create_page(MainPage)
    # Close message if it shows
    main_page.close_message()
    time.sleep(2)
    # Open sidebar
    main_page.open_sidebar()
    time.sleep(2)
    yield main_page
    # Restart app
    page_manager.driver.reset()
