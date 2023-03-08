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

    def test_edit_graininess(self):
        try:
            self.driver.find_element(By.ID, 'tab-resource').click()
            time.sleep(1)
            graininess = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[1]
            formContainerList = graininess.find_elements(By.CLASS_NAME, 'form-container')
            formContainer = formContainerList[0]
            firstForm = formContainer.find_elements(By.CSS_SELECTOR, '.form-section.form-section-resource')[0]
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
                    self.driver.execute_script("arguments[0].scrollIntoView(false);", elInput)
                    content.find_element(By.CLASS_NAME, 'el-icon-circle-close').click()
                    time.sleep(1)
                    elInput.find_element(By.CLASS_NAME, 'el-input__suffix-inner').click()
                    time.sleep(1)
                    selectOption = self.driver.find_elements(By.XPATH,
                                                             '//div[contains(@class, "el-select-dropdown") and  contains(@class, "el-popper")]')
                    selectItem = \
                    selectOption[len(selectOption) - 1].find_elements(By.CSS_SELECTOR, '.el-select-dropdown__item')[0]
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

            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            time.sleep(1)

            graininess = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[1]
            formContainerList = graininess.find_elements(By.CLASS_NAME, 'form-container')
            formContainer = formContainerList[0]
            firstForm = formContainer.find_elements(By.CSS_SELECTOR, '.form-section.form-section-resource')[0]
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
                    currentValue = formItem.find_element(By.CLASS_NAME, 'el-select__tags-text').text
                elif isSpan:
                    currentValue = formItem.find_element(By.TAG_NAME, 'span').text
                else:
                    currentValue = formItem.find_element(By.CLASS_NAME, 'el-input__inner').get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试细粒度表单' + label.replace(':', '') + '表单编辑功能成功!')

        except Exception as e:
            logging.exception(e)

    def test_graininess_remove_and_add(self):
        try:
            self.driver.find_element(By.ID, 'tab-resource').click()
            time.sleep(1)
            operationItems = self.driver.find_elements(By.XPATH,
                                                       '//div[contains(@class, "form-section") and  contains(@class, "form-section-resource")]')

            title = ''
            startPage = ''
            endPage = ''
            for item in operationItems:
                isRemoved = True
                try:
                    item.find_element(By.CLASS_NAME, 'el-icon-close')
                except Exception as e:
                    isRemoved = False
                if not isRemoved:
                    continue

                item.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
                inputList = self.driver.find_elements(By.XPATH,
                                                      '//div[contains(@class, "el-form-item") and not(contains(@class, "el-form-item__content"))]')
                title = inputList[27].find_element(By.CLASS_NAME, 'el-form-item__content').find_element(By.TAG_NAME,
                                                                                                        'span').text
                startPage = inputList[28].find_element(By.CLASS_NAME, 'el-form-item__content').find_element(By.TAG_NAME,
                                                                                                            'span').text
                endPage = inputList[29].find_element(By.CLASS_NAME, 'el-form-item__content').find_element(By.TAG_NAME,
                                                                                                          'span').text
                item.find_element(By.CLASS_NAME, 'el-icon-close').click()
                time.sleep(1)
                confirmModal = self.driver.find_element(By.CLASS_NAME, 'el-message-box__btns')
                confirmModal.find_elements(By.TAG_NAME, 'span')[1].click()
                time.sleep(2)
                try:
                    message = self.driver.find_element(By.CLASS_NAME, 'el-message__content').text
                except Exception as e:
                    message = ''
                self.assertEqual('删除成功！', message, '删除颗粒度记录成功')
                break

            self.driver.find_element(By.XPATH, '//span[text()="新增章节"]').click()
            time.sleep(1)

            inputList = self.driver.find_elements(By.XPATH,
                                                  '//div[contains(@class, "el-form-item") and contains(@class, " is-required")]')
            titleInput = inputList[12].find_element(By.CLASS_NAME, 'el-input__inner')
            titleInput.clear()
            titleInput.send_keys(title)
            startPageInput = inputList[13].find_element(By.CLASS_NAME, 'el-input__inner')
            startPageInput.clear()
            startPageInput.send_keys(startPage)
            endpageInput = inputList[14].find_element(By.CLASS_NAME, 'el-input__inner')
            endpageInput.clear()
            endpageInput.send_keys(endPage)
            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(2)
            try:
                message = self.driver.find_element(By.CLASS_NAME, 'el-message__content').text
            except Exception as e:
                message = ''
            self.assertEqual('保存成功', message, '新增颗粒度记录成功')

            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            time.sleep(1)

        except Exception as e:
            logging.exception(e)

    def test_graininess_count(self):
        try:
            self.driver.find_element(By.ID, 'tab-resource').click()
            time.sleep(1)
            graininess = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[1]
            text = graininess.find_elements(By.CLASS_NAME, 'form-container')[0]
            table = graininess.find_elements(By.CLASS_NAME, 'form-container')[1]

            textItems = text.find_elements(By.CSS_SELECTOR, '.form-section.form-section-resource')
            tableItems = table.find_elements(By.CSS_SELECTOR, '.form-section.form-section-resource')
            operationItems = self.driver.find_elements(By.XPATH,
                                                       '//div[contains(@class, "form-section") and  contains(@class, "form-section-resource")]')

            textCount = self.driver.find_element(By.ID, 'tab-text').text.replace('图文 (', '').replace(')', '')
            tableCount = self.driver.find_element(By.ID, 'tab-table').text.replace('图表 (', '').replace(')', '')
            totalCount = self.driver.find_element(By.ID, 'tab-resource').text.replace('细颗粒度（', '').replace('）', '')
            self.assertEqual(len(textItems), int(textCount), '颗粒度图文计数校验成功')
            self.assertEqual(len(tableItems), int(tableCount), '颗粒度图表计数校验成功')
            self.assertEqual(len(operationItems), int(totalCount), '颗粒度计数校验成功')

        except Exception as e:
            logging.exception(e)

    def test_add_graininess_diagramm(self):
        try:
            self.driver.find_element(By.ID, 'tab-resource').click()
            time.sleep(1)
            self.driver.find_element(By.ID, 'tab-table').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="框选"]').click()
            time.sleep(1)

            canvas = self.driver.find_elements(By.XPATH,
                                               '//div[contains(@class, "cropper-drag-box") and  contains(@class, "cropper-crop")]')[
                0]
            actions = ActionChains(self.driver).move_to_element(canvas)
            actions.perform()
            time.sleep(1)
            pyautogui.moveTo(200, 400, duration=0.5)
            pyautogui.dragTo(250, 450, duration=0.5, button='left')
            time.sleep(1)
            self.driver.find_elements(By.XPATH,
                                      '//div[contains(@class, "item-panel") and  contains(@class, "el-icon-check")]')[
                0].click()
            time.sleep(2)
            try:
                message = self.driver.find_element(By.CLASS_NAME, 'el-message__content').text
            except Exception as e:
                message = ''
            self.assertEqual('成功添加一个图表细颗粒度', message, '添加颗粒度图表记录成功')

        except Exception as e:
            logging.exception(e)

    def test_edit_graininess_diagramm(self):
        try:
            self.driver.find_element(By.ID, 'tab-resource').click()
            time.sleep(1)
            self.driver.find_element(By.ID, 'tab-table').click()
            time.sleep(1)
            graininess = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[1]
            tabTable = graininess.find_elements(By.CLASS_NAME, 'form-container')[1]
            tabTableItemList = []
            try:
                tabTableItemList = tabTable.find_elements(By.CSS_SELECTOR, '.form-section.form-section-resource')
            except Exception as e:
                return
            if len(tabTableItemList) == 0:
                return
            item = tabTableItemList[0]
            item.find_element(By.CLASS_NAME, 'el-icon-edit').click()
            time.sleep(1)
            elForm = item.find_element(By.CLASS_NAME, 'el-form')
            requiredFormItemList = elForm.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required')
            labelValue = {}
            for formItem in requiredFormItemList:
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
                    self.driver.execute_script("arguments[0].scrollIntoView(false);", elInput)
                    content.find_element(By.CLASS_NAME, 'el-icon-circle-close').click()
                    time.sleep(1)
                    elInput.find_element(By.CLASS_NAME, 'el-input__suffix-inner').click()
                    time.sleep(1)
                    selectOption = self.driver.find_elements(By.XPATH,
                                                             '//div[contains(@class, "el-select-dropdown") and  contains(@class, "el-popper")]')
                    selectItem = \
                        selectOption[len(selectOption) - 1].find_elements(By.CSS_SELECTOR, '.el-select-dropdown__item')[
                            0]
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

            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            time.sleep(2)

            tabTableItemList = tabTable.find_elements(By.CSS_SELECTOR, '.form-section.form-section-resource')
            item = tabTableItemList[0]
            item.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
            time.sleep(2)
            elForm = item.find_element(By.CLASS_NAME, 'el-form')
            requiredFormItemList = elForm.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required')

            for formItem in requiredFormItemList:
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
                    currentValue = formItem.find_element(By.CLASS_NAME, 'el-select__tags-text').text
                elif isSpan:
                    currentValue = formItem.find_element(By.TAG_NAME, 'span').text
                else:
                    currentValue = formItem.find_element(By.CLASS_NAME, 'el-input__inner').get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试细粒度表单' + label.replace(':', '') + '表单编辑功能成功!')

        except Exception as e:
            logging.exception(e)

    def test_remove_graininess_diagramm(self):
        try:
            self.driver.find_element(By.ID, 'tab-resource').click()
            time.sleep(1)
            self.driver.find_element(By.ID, 'tab-table').click()
            time.sleep(1)
            graininess = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[1]
            tabTable = graininess.find_elements(By.CLASS_NAME, 'form-container')[1]
            tabTableItemList = []
            try:
                tabTableItemList = tabTable.find_elements(By.CSS_SELECTOR, '.form-section.form-section-resource')
            except Exception as e:
                return

            if len(tabTableItemList) == 0:
                return

            item = tabTableItemList[0]
            item.find_element(By.CLASS_NAME, 'el-icon-close').click()
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
