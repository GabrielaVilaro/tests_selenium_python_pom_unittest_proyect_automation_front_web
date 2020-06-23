#clase de la página index
class PageIndex:
    #constructor con elementos a usar
    def __init__(self, my_driver):
        self.query_top = 'search_query_top'
        self.button_search = 'submit_search'
        self.driver = my_driver

    def search(self, item):
        self.driver.find_element_by_id(self.query_top).send_keys(item)
        self.driver.find_element_by_name(self.button_search).click()
