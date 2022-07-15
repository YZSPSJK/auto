import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import unittest
import logging


class TestCase(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--window-size=1920,1080")
        s = Service('D:/python/python/chromedriver.exe')
        # s = Service('/Users/sjk/workspace/sjk/python/chromedriver')
        self.driver = webdriver.Chrome(service=s, options=chrome_options)
        self.driver.get('http://175.27.232.12:8143/skyrim/#/home')
        time.sleep(1)

    def test_login_required(self):
        try:
            usernameInput = self.driver.find_element(By.NAME, 'username')
            usernameInput.clear()
            usernameInput.send_keys('user1')
            passwordInput = self.driver.find_element(By.NAME, 'password')
            passwordInput.clear()
            passwordInput.send_keys('123456WTW')
            self.driver.find_element(By.CLASS_NAME, 'el-button').click()
            time.sleep(2)
            sidebarTitle = self.driver.find_element(By.CLASS_NAME, 'sidebar-title').text
        except Exception as e:
            sidebarTitle = ''
            logging.exception(e)
        self.assertEqual('后台管理系统', sidebarTitle, '登陆成功')

    def test_reLogin_required(self):
        self.driver.add_cookie(
            {'domain': '175.27.232.12', 'httpOnly': False, 'name': 'skyrim_admin_token', 'path': '/', 'secure': False,
             'value': 'Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiMTAwMyJdLCJ1c2VyX25hbWUiOiJ1c2VyMSIsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJleHAiOjE2NTg5MDM3NTcsImF1dGhvcml0aWVzIjpbIlJPTEVfQURNSU4iXSwianRpIjoiMjFhMjU3ZWMtNjk3ZC00OTdiLTg2MDEtYmZjNDhmYjI3ZjhhIiwiY2xpZW50X2lkIjoibWVzc2FnaW5nLWNsaWVudCJ9.UHtKM_9lG3b1xNoGkjicVM4kJDMdQxxU-2z4-Le0scKtSTfLLK4byV2xvCmaD7Legmd1f9XqgPK9eoOHL798MR0Gv3gwZFDWLRakiOfha2CfDh0HJQTJr5EvxB7NNkFYgf9tiuV2vtI-0vVGNmMyo5oOG1wIHYVptEPuj402-nPCz0gM_VFW4v5Pcn1jKu8JQEREYcQpn8UnBzGCopa7Iap1fykRMkItYlawa21E6PuGYGDS_YMAd5pczpif6L3kk0RTUpddqxJUY9gF9cmz3I7p5SKavZvLceXKyWqcoeuNt7GmD1CiZ-UVXf8tTenReweOiA8GK6D17KrEib0Lyg'})
        self.driver.refresh()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//i[@class="el-icon-caret-bottom"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 '//li[contains(@class, "el-dropdown-menu__item")]/span[text()="退出登录"]').click()
        mainTitle = self.driver.find_element(By.XPATH, '//div[@class="title-container"]/h3').text
        self.assertEqual('管理系统登录', mainTitle, '退出登陆成功')

        try:
            usernameInput = self.driver.find_element(By.NAME, 'username')
            usernameInput.clear()
            usernameInput.send_keys('user1')
            passwordInput = self.driver.find_element(By.NAME, 'password')
            passwordInput.clear()
            passwordInput.send_keys('123456WTW')
            self.driver.find_element(By.CLASS_NAME, 'el-button').click()
            time.sleep(1)
            sidebarTitle = self.driver.find_element(By.CLASS_NAME, 'sidebar-title').text
        except Exception as e:
            sidebarTitle = ''
            logging.exception(e)
        self.assertEqual('后台管理系统', sidebarTitle, '登陆成功')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
