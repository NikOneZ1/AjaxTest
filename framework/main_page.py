from selenium.common.exceptions import NoSuchElementException
from .page import Page


class MainPage(Page):
    elements_id = {'cancel_btn': 'com.ajaxsystems:id/cancel_button',
                   'menu_drawer': 'com.ajaxsystems:id/menuDrawer'}

    def close_message(self):
        # Close message if it shows
        try:
            self.find_element(self.elements_id['cancel_btn']).click()
        except NoSuchElementException:
            pass

    def open_sidebar(self):
        menu_drawer = self.find_element(self.elements_id['menu_drawer'])
        menu_drawer.click()
