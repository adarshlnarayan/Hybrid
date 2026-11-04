class profile:
    contact_detail = '//a[text()="Contact Details"]'

    def __init__(self,driver):
        self.driver = driver

    def click_contact_detail(self):
        self.driver.find_element('xpath',self.contact_detail).click()