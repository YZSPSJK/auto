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
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--window-size=1920,1080")
        # s = Service('D:/python/python/chromedriver.exe')
        s = Service('/Users/sjk/workspace/sjk/python/chromedriver')
        self.driver = webdriver.Chrome(service=s, options=chrome_options)
        self.driver.get('http://117.50.198.51:8880/skyrim/home/my')
        self.driver.add_cookie(
            {'httpOnly': False, 'name': 'skyrim_intelligence_token', 'path': '/', 'secure': False,
             'value': 'Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiMTAwMyJdLCJkZXZpY2VfaWQiOiI3Yjk4NGU3OWJlMWJmZDFjODRiNWQwMzZlYWMwODVkOSIsInVzZXJfbmFtZSI6ImF1dG90ZXN0Iiwic2NvcGUiOlsicmVhZCIsIndyaXRlIl0sImV4cCI6MTY4NDkzODA0MiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9BRE1JTiJdLCJqdGkiOiIzZmM4MzkwMS1iOTIzLTQ5YzctODVmMS1lYTJkN2ZmNTE1Y2EiLCJjbGllbnRfaWQiOiJtZXNzYWdpbmctY2xpZW50IiwiYWRkaXRpb24iOnsiaW5kZXhfc2V0IjoidHJ1ZSJ9fQ.q4zNGgRpX3FvITKA-D9cjIiOTvXJxGtGUbhWLMefRdF4R2vFasKvYNHNcMQ-h0NzoV1nPnU_4LtTMct7Mutf-BRnqXJRU862WDA05pI8DO-_FIOp-1CrJBPIRc0L5IUW1gIgXQkb4TWdqMiQ4yGONV7Gmihg_YxZ6dllh4gYWigQ-890TRMr7vQvfHM1QKfVBr44412NUHFdUfnQkG-nbPlN_GxzCr11prHjZ_bTCTceJemECE5v3MLJPH24msVo8krT1GSOuc1tmVidzUcnW3wQQ77AGJsKBH1sqUAll10ecwBXjgOnQHvckmDVeT3-WimG3PRVoijlwRxWn4u3Hg'})
        self.driver.refresh()
        time.sleep(2)

    def test_tab_switch_manage(self):
        try:

            menuContainer = self.driver.find_element(By.CLASS_NAME, 'navbar-menu-container')
            subMenus = menuContainer.find_elements(By.CLASS_NAME, 'el-sub-menu')
            menuItems = menuContainer.find_elements(By.CLASS_NAME, 'el-menu-item')
            for item in menuItems:
                item.click()
                time.sleep(1)

            i = 0
            for item in subMenus:

                subMenuPopovers = self.driver.find_elements(By.XPATH,
                                                            '//div[contains(@class, "el-popper") and contains(@class, "navbar-submenu")]')
                subMenuItems = subMenuPopovers[i].find_elements(By.CLASS_NAME, 'el-menu-item')
                for subItem in subMenuItems:
                    item.click()
                    time.sleep(1)
                    subItem.click()
                    time.sleep(1)
                i=i+1
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
