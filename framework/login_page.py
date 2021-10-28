import time
from .page import Page


class LoginPage(Page):
    elements_id = {'login_btn': 'com.ajaxsystems:id/login',
                   'email_field': 'com.ajaxsystems:id/login',
                   'password_field': 'com.ajaxsystems:id/password',
                   'next_btn': 'com.ajaxsystems:id/next'}

    def log_in(self, login, password):
        time.sleep(2)
        # Search and click LogIn button on first page
        login_btn = self.find_element(self.elements_id['login_btn'])
        self.click_element(login_btn)
        time.sleep(2)

        # Search for an email field and enter data from parameters into it
        email_field = self.find_element(self.elements_id['email_field'])
        email_field.send_keys(login)

        # Search for an password field and enter data from parameters into it
        password_field = self.find_element(self.elements_id['password_field'])
        password_field.send_keys(password)

        # Search and click button with text LogIn
        next_btn = self.find_element(self.elements_id['next_btn'])
        self.click_element(next_btn)
        time.sleep(3)
