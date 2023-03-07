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
             'value': 'Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiMTAwMyJdLCJ1c2VyX25hbWUiOiJ0ZXN0dXNlciIsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJleHAiOjE2NzkwNjI3NjksImF1dGhvcml0aWVzIjpbIlJPTEVfUk9MRTAwMSIsIlJPTEVfQURNSU4iXSwianRpIjoiMzE1OWQwYjEtNDBjNy00MDliLTgwNWMtZDc4MTRjN2Q0ZjUyIiwiY2xpZW50X2lkIjoibWVzc2FnaW5nLWNsaWVudCIsImFkZGl0aW9uIjpudWxsfQ.OU1kgjeKnQwsKfqw9X7R-JNzGrGwZrhROhzvwGFsVqgI6lsEvZ2pvHPQm6KR8uscmNIkqqi6z9QTw7sVGdPrEPG2VSwnofgZJk7D8071ou4v-4V76oj36nZmSjnypnb4rI6cwU5yNMOIxlZUYhSciKCN_8UbW5MIRaRnt_U3ckQCXge4xYKLTf_ryYBGGhoqqO7ETnD-fitifuh-wHoIdMvKs0M2ZateZFjfsg8kQWUOHBoGvHH54ak_NwwAEipTixTEaouTzDEtfxyTStxcICA50D5ZQstMyRVU3yksvLje-7Gazqcu6Lo2QcHt4iBAw6KXoiiX9fQWu4bvDw_kBg'})
        self.driver.refresh()
        time.sleep(2)
        self.driver.get('http://146.56.203.127:8143/library-test/workbench/180010020230000012')
        time.sleep(2)

    def test_base_info(self):
        try:
            self.driver.find_element(By.XPATH, '//span[text()="编辑"]').click()
            time.sleep(1)
            sectionTitle = self.driver.find_element(By.XPATH, '//div[@class="section-title" and text() = " 工作区 "]')
            baseInfo = sectionTitle.find_elements(By.XPATH, '//div[@class="workbench-content"]')[0]

            requiredFormItemList = baseInfo.find_elements(By.XPATH,

                                                          '//div[contains(@class, "el-form-item") and  contains(@class, "is-required")]')

            labelValue = {}
            for formItem in requiredFormItemList:
                label = formItem.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = formItem.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                elInput = content.find_element(By.CSS_SELECTOR, 'div:first-child')

                isSelect = True
                try:
                    elInput.find_element(By.CSS_SELECTOR, 'div:first-child')
                except Exception as e:
                    isSelect = False

                isInput = True
                try:
                    elInput.find_element(By.CLASS_NAME, 'el-input__inner')
                except Exception as e:
                    isInput = False

                isTextarea = True
                try:
                    elInput.find_element(By.CLASS_NAME, 'el-textarea__inner')
                except Exception as e:
                    isTextarea = False
                if isSelect:
                    self.driver.execute_script("arguments[0].scrollIntoView();", elInput)
                    content.find_element(By.CLASS_NAME, 'el-icon-circle-close').click()
                    time.sleep(1)
                    elInput.find_element(By.CLASS_NAME, 'el-input__suffix-inner').click()
                    time.sleep(1)
                    selectOption = self.driver.find_elements(By.XPATH,
                                                             '//div[contains(@class, "el-select-dropdown") and  contains(@class, "el-popper")]')
                    selectItem = selectOption[6].find_elements(By.CSS_SELECTOR, '.el-select-dropdown__item')[0]
                    selectItem.click()
                    labelValue[label] = selectItem.find_element(By.TAG_NAME, 'span').text
                    time.sleep(1)
                elif isInput:
                    input = elInput.find_element(By.CLASS_NAME, 'el-input__inner')
                    input.clear()
                    input.send_keys('测试' + label.replace(':', ''))
                    labelValue[label] = '测试' + label.replace(':', '')
                elif isTextarea:
                    input = elInput.find_element(By.CLASS_NAME, 'el-textarea__inner')
                    input.clear()
                    input.send_keys('测试' + label.replace(':', ''))
                    labelValue[label] = '测试' + label.replace(':', '')

            baseInfo.find_elements(By.XPATH, '//span[text()="保存"]')[1].click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            time.sleep(1)
            requiredFormItemList = baseInfo.find_elements(By.XPATH,
                                                          '//div[contains(@class, "el-form-item") and  contains(@class, "is-required")]')

            for formItem in requiredFormItemList:
                isTextarea = True
                try:
                    formItem.find_element(By.CLASS_NAME, 'el-textarea__inner')
                except Exception as e:
                    isTextarea = False
                isSelectTag = True
                try:
                    formItem.find_element(By.CLASS_NAME, 'el-select__tags')
                except Exception as e:
                    isSelectTag = False
                label = formItem.find_element(By.CLASS_NAME, 'el-form-item__label').text
                currentValue = ''
                if isTextarea:
                    currentValue = formItem.find_element(By.CLASS_NAME, 'el-textarea__inner').get_attribute('value')
                elif isSelectTag:
                    currentValue = formItem.find_element(By.CLASS_NAME, 'el-select__tags-text').text
                else:
                    currentValue = formItem.find_element(By.CLASS_NAME, 'el-input__inner').get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试' + label.replace(':', '') + '表单编辑功能成功!')
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
