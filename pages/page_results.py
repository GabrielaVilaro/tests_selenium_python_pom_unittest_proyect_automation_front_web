from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class ResultCases:
    def __init__(self, driver):
        self.no_result = (By.XPATH, '//*[@id="center_column"]/p')
        self.title_banner = (By.XPATH, '//*[@id="center_column"]/h1/span[1]')
        self.colour_orange = (By.ID, 'color_1')
        self.select_product = (By.ID, 'selectProductSort')
        self.driver = driver

    def get_text(self):
        text_get = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.no_result))
        text = text_get.text
        return text

    def return_section_title(self):
        section_title = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.title_banner))
        title = section_title.text
        return title

    def select_color(self):
        select_orange = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.colour_orange))
        select_orange.click()

    def product_list_by_select(self, text):
        order = Select(self.driver.find_element(self.select_product))
        order.select_by_visible_text(text)

    def product_list_by_value(self, value):
        order = Select(self.driver.find_element(self.select_product))
        order.select_by_value(value)

    def product_list_by_index(self, number):
        order = Select(self.driver.find_element(self.select_product))
        order.select_by_index(number)

