import datetime

from selenium.webdriver.common.keys import Keys
from pages.basepage import *
from locators.sign_up_locators.locatorSignup import SignupPageLocators, CreateAccountLocators


time_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


class CreateAccount(BasePage):

    def check_already_account_link(self):
        return self.driver.find_element(*CreateAccountLocators.already_account_link).text

    def check_kirv_logo(self):
        return self.driver.find_element(*SignupPageLocators.kirv_logo).is_displayed()

    def check_create_acc_title(self):
        return self.driver.find_element(*CreateAccountLocators.create_account_title).text

    def credential_set_para(self):
        return self.driver.find_element(*CreateAccountLocators.set_credentials_para).text

    def email_error(self):
        return self.driver.find_element(*CreateAccountLocators.email_err).text

    def password_error(self):
        return self.driver.find_element(*CreateAccountLocators.password_err).text

    def confirm_button(self):
        self.driver.find_element(
            *CreateAccountLocators.confirm_btn).click()

    def clear_put_value(self, locator):
        """
        clears and puts input in input box
        """
        time.sleep(2)
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

    def create_account_page_elements(self):
        try:
            assert self.check_kirv_logo() == True
            print("Success: kirv logo found on create account page.")
        except:
            print("No result found for kirv logo in create account page.")

        try:
            assert self.check_create_acc_title() == "Create your account"
            print("Success: create account title found.")
        except:
            print("No result found for create account title.")

        try:
            assert self.credential_set_para() == "Set the credentials for your Kirv account."
            print("Success: create account set credential paragraph found.")
        except:
            print("No result found for create account set credential paragraph.")

        try:
            assert self.check_already_account_link() == "Already have an account?"
            print("Success: create account already have account link found.")
        except:
            print("No result found for create account already have account link.")

        self.confirm_button()
        time.sleep(4)

        try:
            assert self.email_error() == "This field is required."
            print("Success: create account email field is required error found.")
        except:
            print("No result found for email error. ")

        try:
            assert self.password_error() == "This field is required."
            print("Success: create account password field is required error found.")
        except:
            print("No result found for password error. ")

        email_feild = self.driver.find_element(
            *CreateAccountLocators.email_input)

        password_feild = self.driver.find_element(
            *CreateAccountLocators.password_input)

        email_feild.send_keys('amz.test')
        password_feild.send_keys('amz')

        self.confirm_button()
        time.sleep(2)

        try:
            assert self.email_error() == "Enter a valid email address."
            print("Success: create account enter a valid email error found.")
        except:
            print("No result found for enter a valid email. ")

        try:
            assert self.password_error() == "password must be 8 characters or more."
            print("Success: create account password field is required error found.")
        except:
            print("No result found for 8 character password error. ")

        self.clear_put_value(CreateAccountLocators.email_input)

        self.clear_put_value(CreateAccountLocators.password_input)
        password_feild.send_keys('amazatic')

        self.confirm_button()
        time.sleep(2)

        try:
            assert self.email_error() == "This field may not be blank."
            print("Success: create account email field blank error found.")
        except:
            print("No result found for email field blank error. ")

        email_feild.send_keys("amztest18@gmail.com")

        self.confirm_button()
        time.sleep(2)

        try:
            assert self.email_error() == "user with this email address already exists."
            print("Success: create account email user exists error found.")
        except:
            print("No result found for email user exists error. ")

        self.clear_put_value(CreateAccountLocators.email_input)

        email_feild.send_keys("amztest18" + "+" + time_now + "@gmail.com")

        self.clear_put_value(CreateAccountLocators.password_input)

        self.confirm_button()
        time.sleep(2)

        try:
            assert self.password_error() == "This field may not be blank."
            print("Success: create account password field blank error found.")
        except:
            print("No result found for password field blank error. ")

        self.clear_put_value(CreateAccountLocators.email_input)

        email_feild.send_keys("amztest18" + "+" + time_now + "@gmail.com")
        print("Email:", email_feild.get_attribute('value'))

        password_feild.send_keys('amazatic')
        print("Password:", password_feild.get_attribute('value'))

        self.confirm_button()