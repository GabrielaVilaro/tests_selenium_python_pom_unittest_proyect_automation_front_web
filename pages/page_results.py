from selenium.webdriver.support.ui import Select

class ResultCases:
    def __init__(self, driver):
        self.no_result = '//*[@id="center_column"]/p'
        self.title_banner = '//*[@id="center_column"]/h1/span[1]'
        self.colour_orange = 'color_1'
        self.driver = driver
        self.select_product = 'selectProductSort'

    def get_text(self):
        return self.driver.find_element_by_xpath(self.no_result).text

    def return_section_title(self):
        return self.driver.find_element_by_xpath(self.title_banner).text

    def select_color(self):
        self.driver.find_element_by_id(self.colour_orange).click()

    def product_list_by_select(self, text):
        order = Select(self.driver.find_element_by_id(self.select_product))
        order.select_by_visible_text(text)

    def product_list_by_value(self, value):
        order = Select(self.driver.find_element_by_id(self.select_product))
        order.select_by_value(value)

    def product_list_by_index(self, number):
        order = Select(self.driver.find_element_by_id(self.select_product))
        order.select_by_index(number)

