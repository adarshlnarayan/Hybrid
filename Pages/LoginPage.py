class Login:
    username = "username"
    password = "password"
    login_btn = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def login(self,un,pwd):
        self.driver.find_element('name',self.username).clear()
        self.driver.find_element('name',self.password).clear()
        self.driver.find_element('name',self.username).send_keys(un)
        self.driver.find_element('name',self.password).send_keys(pwd)
        self.driver.find_element('xpath',self.login_btn).click()
