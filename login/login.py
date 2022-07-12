import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest


class TestCase(unittest.TestCase):

    @staticmethod
    def login():
        s = Service('/Users/sjk/workspace/sjk/python/auto/chromedriver')
        driver = webdriver.Chrome(service=s)

        driver.get('http://175.27.232.12:8143/skyrim/#/login?redirect=%2Fhome')

        time.sleep(1)

        try:
            usernameInput = driver.find_element(By.NAME, 'username')
            usernameInput.clear()
            usernameInput.send_keys('user1')
            passwordInput = driver.find_element(By.NAME, 'password')
            passwordInput.clear()
            passwordInput.send_keys('123456WTW')

            driver.find_element(By.CLASS_NAME, 'el-button').click()

            time.sleep(1)
            print('测试')

            sidebarTitle = driver.find_element(By.CLASS_NAME, 'sidebar-title')
            result = sidebarTitle.text
        except Exception as e:
            result = ''
        finally:
            driver.quit()
        return result

    def test_login_required(self):
        sidebarTitle = self.login()
        self.assertEqual('后台管理系统', sidebarTitle, '登陆成功')


if __name__ == '__main__':
    unittest.main()
