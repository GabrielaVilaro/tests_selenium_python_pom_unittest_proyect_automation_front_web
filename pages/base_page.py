class BasePage(object):
    def __init__(self, driver='../driver/chromedriver', base_url='http://automationpractice.com/index.php'):
        self.driver = driver
        self.base_url = base_url



