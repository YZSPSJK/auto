import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import unittest
import logging
from BeautifulReport import BeautifulReport


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
        self.driver.add_cookie(
            {'domain': '175.27.232.12', 'httpOnly': False, 'name': 'skyrim_admin_token', 'path': '/', 'secure': False,
             'value': 'Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiMTAwMyJdLCJ1c2VyX25hbWUiOiJ1c2VyMSIsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJleHAiOjE2NTg5MDM3NTcsImF1dGhvcml0aWVzIjpbIlJPTEVfQURNSU4iXSwianRpIjoiMjFhMjU3ZWMtNjk3ZC00OTdiLTg2MDEtYmZjNDhmYjI3ZjhhIiwiY2xpZW50X2lkIjoibWVzc2FnaW5nLWNsaWVudCJ9.UHtKM_9lG3b1xNoGkjicVM4kJDMdQxxU-2z4-Le0scKtSTfLLK4byV2xvCmaD7Legmd1f9XqgPK9eoOHL798MR0Gv3gwZFDWLRakiOfha2CfDh0HJQTJr5EvxB7NNkFYgf9tiuV2vtI-0vVGNmMyo5oOG1wIHYVptEPuj402-nPCz0gM_VFW4v5Pcn1jKu8JQEREYcQpn8UnBzGCopa7Iap1fykRMkItYlawa21E6PuGYGDS_YMAd5pczpif6L3kk0RTUpddqxJUY9gF9cmz3I7p5SKavZvLceXKyWqcoeuNt7GmD1CiZ-UVXf8tTenReweOiA8GK6D17KrEib0Lyg'})
        self.driver.refresh()
        time.sleep(1)

    def test_tab_switch_manage(self):
        try:
            self.driver.find_element(By.XPATH, '//span[text()="系统管理"]').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="账户管理"]').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="应用管理"]').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="字典管理"]').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="机构管理"]').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="角色管理"]').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="资源管理"]').click()
            time.sleep(1)

            tabAccountManage = self.driver.find_element(By.XPATH,
                                                        '//span[contains(@class, "tags-view-item") and contains(text(), "账户管理")]')
            tabAccountManage.click()
            time.sleep(1)
            mainTitle = self.driver.find_element(By.XPATH, '//div[@class="main_title"]/p').text
            self.assertIn('账户管理', mainTitle, 'tab页切换功能正常')
            time.sleep(1)
            tabApplicationManage = self.driver.find_element(By.XPATH,
                                                            '//span[contains(@class, "tags-view-item") and contains(text(), "应用管理")]')
            tabApplicationManage.click()
            time.sleep(1)
            mainTitle = self.driver.find_element(By.XPATH, '//div[@class="main_title"]/p').text
            self.assertIn('应用管理', mainTitle, 'tab页切换功能正常')
            time.sleep(1)
            tabDirectoryManage = self.driver.find_element(By.XPATH,
                                                          '//span[contains(@class, "tags-view-item") and contains(text(), "字典管理")]')
            tabDirectoryManage.click()
            time.sleep(1)
            mainTitle = self.driver.find_element(By.XPATH, '//div[@class="main_title"]/p').text
            self.assertIn('字典管理', mainTitle, 'tab页切换功能正常')
            time.sleep(1)
            tabOrgManage = self.driver.find_element(By.XPATH,
                                                    '//span[contains(@class, "tags-view-item") and contains(text(), "机构管理")]')
            tabOrgManage.click()
            time.sleep(1)
            mainTitle = self.driver.find_element(By.XPATH, '//div[@class="right_title"]/p').text
            self.assertIn('组织机构列表', mainTitle, 'tab页切换功能正常')
            time.sleep(1)
            tabRoleManage = self.driver.find_element(By.XPATH,
                                                     '//span[contains(@class, "tags-view-item") and contains(text(), "角色管理")]')
            tabRoleManage.click()
            time.sleep(1)
            mainTitle = self.driver.find_element(By.XPATH, '//div[@class="main_title"]/p').text
            self.assertIn('角色管理', mainTitle, 'tab页切换功能正常')
            time.sleep(1)
            tabSourceManage = self.driver.find_element(By.XPATH,
                                                       '//span[contains(@class, "tags-view-item") and contains(text(), "资源管理")]')
            tabSourceManage.click()
            time.sleep(1)
            mainTitle = self.driver.find_element(By.XPATH, '//div[@class="right_title"]/p').text
            self.assertIn('资源列表', mainTitle, 'tab页切换功能正常')
        except Exception as e:
            logging.exception(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestCase))
    br = BeautifulReport(suite)
    br.report(filename='tabSwitch.html', description='测试报告',
              report_dir='/Users/sjk/workspace/sjk/python/auto/testReport')
