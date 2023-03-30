import time

import pyautogui as pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import unittest
import logging
from BeautifulReport import BeautifulReport


class TestCase(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--window-size=1920,1080")
        # s = Service('D:/python/python/chromedriver.exe')
        s = Service('/Users/sjk/workspace/sjk/python/chromedriver')
        self.driver = webdriver.Chrome(service=s, options=chrome_options)
        self.driver.get('http://146.56.203.127:8143/library-test/home')
        self.driver.add_cookie(
            {'domain': '146.56.203.127', 'httpOnly': False, 'name': 'library_admin_token', 'path': '/', 'secure': False,
             'value': 'Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiMTAwMyJdLCJ1c2VyX25hbWUiOiJ0ZXN0dXNlciIsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJleHAiOjE2ODI0MjczMDksImF1dGhvcml0aWVzIjpbIlJPTEVfUk9MRTAwMSIsIlJPTEVfQURNSU4iXSwianRpIjoiMzZjODI4MWMtYzVmNC00MGM0LTgzOGEtMTM3NzhlNmEzMGIyIiwiY2xpZW50X2lkIjoibWVzc2FnaW5nLWNsaWVudCIsImFkZGl0aW9uIjpudWxsfQ.CAJ3vuakeW70HPRQRYSaFFrRGItR6wf16ch0cPlUqXoUyLXnBfUALnpx3zIBbHIG78Jw7RJBBXWitbNVtcz32muW1QK2ngHWeZd0jbXM0WJM3WzIWPJPS2lnb_u059PWLb-c9-fR4uyxSt9Rd1zQ4TrlvCIMocYw76B9WpFjyD2jJxi7iEeJ_0A7a3us64WSBVwlAH1DZq8oJa00BEo8tAl_4CJVaTXGOHNKmB7Zjd0Me3TubhDaFSlxboOTJbNtfufBF0VpGTPYxU0fLC3wo2VH1U-UcFBKjg7BaGthmsXT--5TRVHN5p4buNdTtZKNKDAd1DfFag3irUw5PMA3vQ'})
        self.driver.refresh()
        time.sleep(2)
        self.driver.get('http://146.56.203.127:8143/library-test/workbench/book/180010020230000012')
        time.sleep(2)

    def test_edit_text(self):
        try:
            self.driver.find_elements(By.XPATH, '//i[@class = "el-icon-edit"]')[0].click()
            time.sleep(1)

            editTextAreaDiv = self.driver.find_element(By.XPATH,
                                                       '//div[contains(@class, "section-wrapper-main") and  contains(@class, "edit-txt")]')
            elTextArea = editTextAreaDiv.find_element(By.CLASS_NAME, 'el-textarea__inner')
            editText = elTextArea.get_attribute('value')
            elTextArea.clear()
            elTextArea.send_keys('测试文本编辑功能')
            self.driver.find_elements(By.XPATH, '//span[text()="保存"]')[1].click()
            time.sleep(3)
            firstFile = self.driver.find_element(By.ID, 'file1')

            self.assertEqual(firstFile.text.replace(' ', ''), '测试文本编辑功能',
                             '测试编辑文本区功能成功!')
        except Exception as e:
            logging.exception(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestCase))
    br = BeautifulReport(suite)
    br.report(filename='sourceList.html', description='测试报告',
              report_dir='/Users/sjk/workspace/sjk/python/auto/testReport')
