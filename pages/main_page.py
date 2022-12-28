from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .base_page import BasePage
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        # *MainPageLocators.LOGIN_LINK - подтягиваем ссылку, указанную в файле locators
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    # обработка исключения в случае ненахождения элемента.
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
