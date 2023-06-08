"""
This class consists of actions (methods) that can be performed using web elements (locators).
"""

import re
from selenium.common import NoSuchElementException
from src.frontend_testing.locators.add_user_locators import AddUserLocators
from src.frontend_testing.pages.base_page import BasePage


class AddUserPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        """
        Methods to check if the form is empty before completing.
        There are two methods that check if the buttons exist on the page.
        Methods used in AddUserTest class.
        """

    def name_field_has_no_input(self):
        if self.driver.find_element(*AddUserLocators.name).get_attribute('value') == '':
            return True

    def user_name_field_has_no_input(self):
        if self.driver.find_element(*AddUserLocators.user_name).get_attribute('value') == '':
            return True

    def email_address_field_has_no_input(self):
        if self.driver.find_element(*AddUserLocators.email_address).get_attribute('value') == '':
            return True

    def phone_number_field_has_no_input(self):
        if self.driver.find_element(*AddUserLocators.phone_number).get_attribute('value') == '':
            return True

    def add_user_button_is_present(self):
        try:
            self.driver.find_element(*AddUserLocators.add_user)
        except NoSuchElementException:
            return False
        return True

    def cancel_button_is_present(self):
        try:
            self.driver.find_element(*AddUserLocators.cancel)
        except NoSuchElementException:
            return False
        return True

    """
    Methods to complete the fields.
    """

    def enter_name(self, name):
        self.driver.find_element(*AddUserLocators.name).send_keys(name)

    def enter_user_name(self, user_name):
        self.driver.find_element(*AddUserLocators.user_name).send_keys(user_name)

    def enter_email_address(self, email_address):
        self.driver.find_element(*AddUserLocators.email_address).send_keys(email_address)

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*AddUserLocators.phone_number).send_keys(phone_number)

    def click_add_user_button(self):
        self.driver.find_element(*AddUserLocators.add_user).click()

    def click_cancel_button(self):
        self.driver.find_element(*AddUserLocators.cancel).click()

    """
    Methods to check if the fields are completed with the expected values.
    """

    def get_input_value(self, field, value):
        if field == 'name':
            if self.driver.find_element(*AddUserLocators.name).get_attribute('value') == value:
                return True
        elif field == 'username':
            if self.driver.find_element(*AddUserLocators.user_name).get_attribute('value') == value:
                return True
        elif field == 'phone':
            if self.driver.find_element(*AddUserLocators.phone_number).get_attribute('value') == value:
                return True

    # Static method to check if the email address is valid
    @staticmethod
    def check_valid_email(address):
        # A regular expression for validating the email address
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(pattern, address):
            return True
        else:
            return False

    def get_input_email(self, value):
        if self.driver.find_element(*AddUserLocators.email_address).get_attribute('value') == value:
            if self.check_valid_email(value):
                return True

    # Static method to check if the phone number is valid
    @staticmethod
    def check_valid_phone_number(phone):
        # phone = phonenumbers.parse(phone)
        # if phonenumbers.is_possible_number(phone):
        pattern = '^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$'
        if re.match(pattern, phone):
            return True
        else:
            return False

    def get_input_phone_number(self, value):
        if self.driver.find_element(*AddUserLocators.phone_number).get_attribute('value') == value:
            if self.check_valid_phone_number(value):
                return True
