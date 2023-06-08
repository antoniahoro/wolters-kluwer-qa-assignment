"""
This class stores the web elements present on Add Users page.
"""

from selenium.webdriver.common.by import By


class AddUserLocators:
    name = (By.XPATH, '/html/body/div/div/div/div/div[1]/div/input')
    user_name = (By.XPATH, '/html/body/div/div/div/div/div[2]/div/input')
    email_address = (By.XPATH, '/html/body/div/div/div/div/div[3]/div/input')
    phone_number = (By.XPATH, '/html/body/div/div/div/div/div[4]/div/input')

    add_user = (By.XPATH, '/html/body/div/div/div/div/div[5]/button[1]/span[1]')
    cancel = (By.XPATH, '/html/body/div/div/div/div/div[5]/button[2]/span[1]')

