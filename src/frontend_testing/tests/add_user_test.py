"""
This class consists of:
1. a setUp() method - to initialize the local driver variable with the actual driver
2. test_add_user_page_elements - a test to check:
    - if all the fields are empty before completing them
    - if the buttons exist
3. test_add_user_add - a test to check if a new user can be added
4. test_add_user_cancel - a test to check if it's possible to cancel adding a new user

Functional Requirements
User creation
1. A new User with the following information can be added: name, phone number, username and email from a simple form
4. We should be able to cancel adding a new user

"""

import unittest
import time
from selenium import webdriver
from src.frontend_testing.pages.add_user_page import AddUserPage


class AddUserTest(unittest.TestCase):
    def setUp(self):
        self.my_driver = webdriver.Chrome()
        self.my_driver.get('http://localhost:3000/add')
        self.my_driver.implicitly_wait(3)

    def test_add_user_page_elements(self):
        self.add_user_page = AddUserPage(self.my_driver)

        # Fields are empty
        assert self.add_user_page.name_field_has_no_input()
        time.sleep(1)
        assert self.add_user_page.user_name_field_has_no_input()
        time.sleep(1)
        assert self.add_user_page.email_address_field_has_no_input()
        time.sleep(1)
        assert self.add_user_page.phone_number_field_has_no_input()
        time.sleep(1)

        # Buttons exist
        assert self.add_user_page.add_user_button_is_present()
        time.sleep(1)
        assert self.add_user_page.cancel_button_is_present()
        time.sleep(1)

    def test_add_user_add(self):
        # Test values
        name_value = 'Anto'
        username_value = 'anto_horo'
        email_value = 'anto_horo@gmail.com'
        phone_value = '333-456-7890'

        # Object that lets us use methods from AddUserPage class
        self.add_user_page = AddUserPage(self.my_driver)

        """
        Check if the page is ready to use.
        """

        self.test_add_user_page_elements()
        time.sleep(1)

        """
        Complete the fields.
        Check if expected result = actual result.
        """

        self.add_user_page.enter_name(name_value)
        time.sleep(3)
        assert self.add_user_page.get_input_value('name', name_value)

        self.add_user_page.enter_user_name(username_value)
        time.sleep(3)
        assert self.add_user_page.get_input_value('username', username_value)

        self.add_user_page.enter_email_address(email_value)
        time.sleep(3)
        assert self.add_user_page.get_input_email(email_value)

        self.add_user_page.enter_phone_number(phone_value)
        time.sleep(3)
        assert self.add_user_page.get_input_phone_number(phone_value)

        # Add new user
        self.add_user_page.click_add_user_button()
        time.sleep(5)

    def test_add_user_cancel(self):
        self.add_user_page = AddUserPage(self.my_driver)

        self.test_add_user_page_elements()
        time.sleep(1)

        self.add_user_page.enter_name('Anto')
        time.sleep(3)
        assert self.add_user_page.get_input_value('name', 'Anto')

        self.add_user_page.enter_user_name('anto_horo')
        time.sleep(3)
        assert self.add_user_page.get_input_value('username', 'anto_horo')

        self.add_user_page.enter_email_address('anto_horo@gmail.com')
        time.sleep(3)
        assert self.add_user_page.get_input_email('anto_horo@gmail.com')

        self.add_user_page.enter_phone_number('333-456-7890')
        time.sleep(3)
        assert self.add_user_page.get_input_phone_number('333-456-7890')

        # Cancel adding a new user
        self.add_user_page.click_cancel_button()
        time.sleep(3)
