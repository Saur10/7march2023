import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest

class Test_Login(BaseTest):

    def test_login_button_visible(self):
        self.LP = LoginPage(self.driver)
        flag=self.LP.is_signup_visible()
        assert flag

    def test_login_page_title(self):
        self.lp= LoginPage(self.driver)
        title=self.lp.get_login_title(TestData.Login_Page_Title)
        assert title ==TestData.Login_Page_Title

    def test_login(self):
        self.lp = LoginPage(self.driver)
        self.lp.do_login(TestData.user_name,TestData.password)




















