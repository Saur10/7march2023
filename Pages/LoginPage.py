from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class LoginPage(BasePage):

    "By locator"
    UserName = (By.CSS_SELECTOR, 'input[name="user-name"]')
    Password = (By.CSS_SELECTOR, 'input[id="password"]')
    Login_button = (By.CSS_SELECTOR, 'input[id="login-button"]')
    singup_link= (By.CSS_SELECTOR, 'input[id="login-button"]')

    "define constructor of the page class"
    def __init__(self,driver):
        super().__init__(driver)

    "Action Class "

    def get_login_title(self,title):
        return self.get_title(title)

    def is_signup_visible(self):
        return self.is_visible(self.singup_link)

    "This is used to login to App"

    def do_login(self, username, password):
        self.do_send_Key(self.UserName, username)
        self.do_send_Key(self.Password, password)
        self.do_click(self.Login_button)


















