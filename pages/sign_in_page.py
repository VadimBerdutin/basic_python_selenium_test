class SignInPage():

    def __init__(self, driver):
        self.driver = driver

    def create_account_click(self):
        create_account_button = self.driver.find_element_by_xpath("//*[text()='Создать аккаунт']")
        create_account_button.click()

    def for_myself_click(self):
        for_myself_button = self.driver.find_element_by_xpath("//*[text()='Для себя']")
        for_myself_button.click()

