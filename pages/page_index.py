from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# clase de la página index
class PageIndex:
    # constructor con elementos a usar
    def __init__(self, driver):
        # ejemplo de como usar la librería BY
        self.query_top = (By.ID, 'search_query_top')
        self.button_search = (By.NAME, 'submit_search')
        self.button_sign_in = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        self.phone_numbre_of_banner = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/span/strong')
        self.driver = driver

    def search(self, item):
        try:
            # probando la librería webdriverwaitt
            box_search = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.query_top))
            box_search.send_keys(item)
            button_search = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_search))
            button_search.click()

        except:
            print("No se encuentra el elemento")

    def push_sign_in(self):
        button_sign_in = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_sign_in))
        button_sign_in.click()

    def return_phone_number_of_banner(self):
        phone_number = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.phone_numbre_of_banner))
        number = phone_number.text
        return number
