class home:
    admin = '//span[text()="Admin"]'
    my_info = '//span[text()="My Info"]'

    def __init__(self,driver):
        self.driver = driver

    def click_info(self):
        self.driver.find_element('xpath',self.my_info).click()

