
class BaseClass:
    def __init__(self, driver):
        self.driver = driver


    def go_to_page(self ,url):
        return self.driver.get(url)
