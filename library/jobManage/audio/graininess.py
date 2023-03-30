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
        self.driver.get('http://146.56.203.127:8143/library-test/workbench/audio/180010020230000379')
        time.sleep(2)

    def test_graininess_count(self):
        try:
            self.driver.find_element(By.ID, 'tab-resource').click()
            time.sleep(1)
            graininess = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[1]

            operationItems = graininess.find_elements(By.CSS_SELECTOR, '.form-section.form-section-resource')
            totalCount = self.driver.find_element(By.ID, 'tab-resource').text.replace('细颗粒度（', '').replace('）', '')
            self.assertEqual(len(operationItems), int(totalCount), '颗粒度计数校验成功')
        except Exception as e:
            logging.exception(e)

    def test_add_graininess(self):
        try:
            self.driver.find_element(By.ID, 'tab-resource').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="新建责任者"]').click()
            time.sleep(1)
            graininess = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[1]
            formContainerList = graininess.find_elements(By.CLASS_NAME, 'form-container')
            formContainer = formContainerList[0]
            allForm = formContainer.find_elements(By.CSS_SELECTOR, '.form-section.form-section-resource')
            firstForm = allForm[len(allForm) - 1]
            labelValue = {}
            for formItem in firstForm.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):

                label = formItem.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = formItem.find_element(By.CSS_SELECTOR, '.el-form-item__content')

                isSpan = False
                try:
                    content.find_element(By.CSS_SELECTOR, 'div:first-child')
                except Exception as e:
                    isSpan = True

                if isSpan:
                    continue

                elInput = content.find_element(By.CSS_SELECTOR, 'div:first-child')
                isSelect = True
                try:
                    elInput.find_element(By.CSS_SELECTOR, '.el-select')
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
                    self.driver.execute_script("arguments[0].scrollIntoView(false);", elInput)

                    try:
                        content.find_element(By.CLASS_NAME, 'el-icon-circle-close').click()
                    except Exception as e:
                        print(e)

                    time.sleep(1)
                    elInput.find_element(By.CLASS_NAME, 'el-input__suffix-inner').click()
                    time.sleep(1)
                    selectOption = self.driver.find_elements(By.XPATH,
                                                             '//div[contains(@class, "el-select-dropdown") and  contains(@class, "el-popper")]')
                    selectItem = \
                    selectOption[len(selectOption) - 1].find_elements(By.CSS_SELECTOR, '.el-select-dropdown__item')[0]
                    selectItem.click()
                    formItem.find_element(By.CLASS_NAME, 'el-form-item__label').click()
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

            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            time.sleep(2)

            graininess = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[1]
            formContainerList = graininess.find_elements(By.CLASS_NAME, 'form-container')
            formContainer = formContainerList[0]
            allForm = formContainer.find_elements(By.CSS_SELECTOR, '.form-section.form-section-resource')
            firstForm = allForm[len(allForm) - 1]
            firstForm.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
            time.sleep(1)
            for formItem in firstForm.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = formItem.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = formItem.find_element(By.CSS_SELECTOR, '.el-form-item__content')

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

                isSpan = False
                try:
                    content.find_element(By.CSS_SELECTOR, 'div:first-child')
                except Exception as e:
                    isSpan = True

                if isSpan:
                    continue

                currentValue = ''
                if isTextarea:
                    currentValue = formItem.find_element(By.CLASS_NAME, 'el-textarea__inner').get_attribute('value')
                elif isSelectTag:
                    print(label)
                    currentValue = formItem.find_element(By.CLASS_NAME, 'el-select__tags-text').text
                elif isSpan:
                    currentValue = formItem.find_element(By.TAG_NAME, 'span').text
                else:
                    currentValue = formItem.find_element(By.CLASS_NAME, 'el-input__inner').get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试细粒度表单' + label.replace(':', '') + '表单新增功能成功!')
        except Exception as e:
            logging.exception(e)



    def test_edit_graininess(self):
        try:
            self.driver.find_element(By.ID, 'tab-resource').click()
            time.sleep(1)
            graininess = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[1]
            formContainerList = graininess.find_elements(By.CLASS_NAME, 'form-container')
            formContainer = formContainerList[0]
            allForm = formContainer.find_elements(By.CSS_SELECTOR, '.form-section.form-section-resource')
            firstForm = allForm[len(allForm)-1]
            firstForm.find_element(By.CLASS_NAME, 'el-icon-edit').click()
            time.sleep(1)
            labelValue = {}
            for formItem in firstForm.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):

                label = formItem.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = formItem.find_element(By.CSS_SELECTOR, '.el-form-item__content')

                isSpan = False
                try:
                    content.find_element(By.CSS_SELECTOR, 'div:first-child')
                except Exception as e:
                    isSpan = True

                if isSpan:
                    continue

                elInput = content.find_element(By.CSS_SELECTOR, 'div:first-child')
                isSelect = True
                try:
                    elInput.find_element(By.CSS_SELECTOR, '.el-select')
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
                    self.driver.execute_script("arguments[0].scrollIntoView(false);", elInput)

                    try:
                        content.find_element(By.CLASS_NAME, 'el-icon-circle-close').click()
                    except Exception as e:
                        print(e)

                    time.sleep(1)
                    elInput.find_element(By.CLASS_NAME, 'el-input__suffix-inner').click()
                    time.sleep(1)
                    selectOption = self.driver.find_elements(By.XPATH,
                                                             '//div[contains(@class, "el-select-dropdown") and  contains(@class, "el-popper")]')
                    selectItem = \
                    selectOption[len(selectOption) - 1].find_elements(By.CSS_SELECTOR, '.el-select-dropdown__item')[0]
                    selectItem.click()
                    formItem.find_element(By.CLASS_NAME, 'el-form-item__label').click()
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

            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            time.sleep(1)

            graininess = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[1]
            formContainerList = graininess.find_elements(By.CLASS_NAME, 'form-container')
            formContainer = formContainerList[0]
            allForm = formContainer.find_elements(By.CSS_SELECTOR, '.form-section.form-section-resource')
            firstForm = allForm[len(allForm) - 1]
            firstForm.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
            time.sleep(1)
            for formItem in firstForm.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = formItem.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = formItem.find_element(By.CSS_SELECTOR, '.el-form-item__content')

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

                isSpan = False
                try:
                    content.find_element(By.CSS_SELECTOR, 'div:first-child')
                except Exception as e:
                    isSpan = True

                if isSpan:
                    continue

                currentValue = ''
                if isTextarea:
                    currentValue = formItem.find_element(By.CLASS_NAME, 'el-textarea__inner').get_attribute('value')
                elif isSelectTag:
                    print(label)
                    currentValue = formItem.find_element(By.CLASS_NAME, 'el-select__tags-text').text
                elif isSpan:
                    currentValue = formItem.find_element(By.TAG_NAME, 'span').text
                else:
                    currentValue = formItem.find_element(By.CLASS_NAME, 'el-input__inner').get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试细粒度表单' + label.replace(':', '') + '表单编辑功能成功!')

        except Exception as e:
            logging.exception(e)

    def test_graininess_remove(self):
        try:
            self.driver.find_element(By.ID, 'tab-resource').click()
            time.sleep(1)
            graininess = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[1]
            formContainerList = graininess.find_elements(By.CLASS_NAME, 'form-container')
            formContainer = formContainerList[0]
            allForm = formContainer.find_elements(By.CSS_SELECTOR, '.form-section.form-section-resource')
            firstForm = allForm[len(allForm) - 1]
            firstForm.find_element(By.CLASS_NAME, 'el-icon-close').click()
            time.sleep(1)
            confirmModal = self.driver.find_element(By.CLASS_NAME, 'el-message-box__btns')
            confirmModal.find_elements(By.TAG_NAME, 'span')[1].click()
            time.sleep(2)
            try:
                message = self.driver.find_element(By.CLASS_NAME, 'el-message__content').text
            except Exception as e:
                message = ''
            self.assertEqual('删除成功！', message, '删除颗粒度图表记录成功')
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
