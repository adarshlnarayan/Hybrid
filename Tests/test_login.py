import time
from Utilities.excel_reader import read_login_data
from Pages.LoginPage import Login
from Pages.homepage import home
from Pages.profile_page import profile


def test_orangehrm(setup):
    driver = setup
    l = Login(driver)
    h = home(driver)
    p = profile(driver)

    data_path = r'C:\Users\adars\PycharmProjects\Hybrid\Test data\selenium ddt.xlsx'
    login_data = read_login_data(data_path,"Sheet2")

    for un, pwd in login_data:
        l.login(un,pwd)
        time.sleep(2)
        if'dashboard' not in driver.current_url:
            driver.get_screenshot_as_file(r'C:\Users\adars\PycharmProjects\Hybrid\ScreenShots\fail.png')
            print('Login failed')
        else:
            print('Login successful')
            h.click_info()
            time.sleep(2)

            p.click_contact_detail()
            time.sleep(2)

            driver.find_element('xpath','//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i').click()
            driver.find_element('xpath','//a[text()="Logout"]').click()
time.sleep(2)
