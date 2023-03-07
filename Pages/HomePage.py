
# 4th-Aug============
# User : Problem user
# URLhttps://www.saucedemo.com/
# 1. Login with Problem user
# 2. Land on Product page
# 3. Print Sauce Labs Backpack
# 4. Get Price from the page
# 5. dd to cart this product
# 6. Remove the product from Add to cart page
# 7. logout and quite the browser
# ========================

from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    menu_bar_link=(By.XPATH,'//a[@id="item_4_title_link"] ')
    item_price_xpath=(By.XPATH,'//div[@class="inventory_item"]')



    #3. Print Sauce Labs Backpack

    def print_backpack(self):
        return self.get_element_text(self.menu_bar_link)












