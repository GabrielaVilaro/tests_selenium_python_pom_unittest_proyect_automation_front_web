class ResultCases:
    def __init__(self, my_driver):
        self.no_result = '//*[@id="center_column"]/p'
        self.title_banner = '//*[@id="center_column"]/h1/span[1]'
        self.colour_orange = 'color_1'
        self.driver = my_driver

    def get_text(self):
        return self.driver.find_element_by_xpath(self.no_result).text

    def return_section_title(self):
        return self.driver.find_element_by_xpath(self.title_banner).text

    def select_color(self):
        self.driver.find_element_by_id(self.colour_orange).click()
