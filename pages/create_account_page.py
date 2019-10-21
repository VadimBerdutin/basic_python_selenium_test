class CreateAccountPage():

    def __init__(self, driver):
        self.driver = driver

    validation_error = "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)."

    def enter_first_name(self, first_name):
        first_name_field = self.driver.find_element_by_id("firstName")
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self.driver.find_element_by_id("lastName")
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_user_name(self, user_name):
        username_field = self.driver.find_element_by_id("username")
        username_field.clear()
        username_field.send_keys(user_name)

    def enter_password(self, password):
        password_field = self.driver.find_element_by_name("Passwd")
        password_field.clear()
        password_field.send_keys(password)

    def enter_confirm_password(self, confirm_password):
        confirm_password_field = self.driver.find_element_by_name("ConfirmPasswd")
        confirm_password_field.clear()
        confirm_password_field.send_keys(confirm_password)

    def click_next(self):
        next_button = self.driver.find_element_by_id("accountDetailsNext")
        next_button.click()
