from selenium import webdriver
import time
from pages.sign_in_page import SignInPage
from pages.create_account_page import CreateAccountPage

driver = webdriver.Chrome("D:/Tools/chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://accounts.google.com")

email_list = ['@q.q', 'q@-q.q', 'q@q', 'q@qq.q']
user_dictionary = {'fn': 'Vadim', 'ln': 'Berdutin', 'password': 'Abc123456!'}

sign_in_page = SignInPage(driver)
sign_in_page.create_account_click()
time.sleep(1)
sign_in_page.for_myself_click()
create_account_page = CreateAccountPage(driver)
create_account_page.enter_first_name(user_dictionary['fn'])
create_account_page.enter_last_name(user_dictionary['ln'])
create_account_page.enter_user_name(email_list[0])
create_account_page.enter_password(user_dictionary['password'])
create_account_page.enter_confirm_password(user_dictionary['password'])
create_account_page.click_next()
time.sleep(1)
assert create_account_page.validation_error in driver.page_source


def validate_username_field(user_name):
    create_account_page.enter_user_name(user_name)
    create_account_page.click_next()
    time.sleep(1)
    assert create_account_page.validation_error in driver.page_source


for user_name in email_list:
    validate_username_field(user_name)

driver.quit()
