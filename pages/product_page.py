from selenium.webdriver.common.by import By

from Stepik_project.pages.base_page import BasePage
from Stepik_project.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_link.click()

    def should_be_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Basket link is not presented"

    def added_to_basket(self):
        product_name = self.browser.find_element(By.XPATH, './/div[@class="col-sm-6 product_main"]/h1').text
        product_name_in_basket = self.browser.find_element(By.XPATH, './/div[@class="alertinner "]/strong').text
        assert product_name == product_name_in_basket, "Названия товара не соответствуют друг другу"

    def compare_costs(self):
        cost_in_basket = self.browser.find_element(By.XPATH, './/div[@class="alertinner "]/p/strong').text
        cost_on_card = self.browser.find_element(By.XPATH, './/p[@class="price_color"]').text
        assert cost_in_basket == cost_on_card, "Цены не соответствуют друг другу"

