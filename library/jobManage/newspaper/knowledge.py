import time
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
        self.driver.get('http://146.56.203.127:8143/library-test/workbench/newspaper/180010020230000376')
        time.sleep(2)

    def test_config_knowledge_person(self):
        try:
            canvas = self.driver.find_elements(By.CLASS_NAME, 'files-page')[0]
            canvas.find_element(By.TAG_NAME, 'pre')
            actions = ActionChains(self.driver).move_to_element(canvas).click_and_hold().move_by_offset(100,
                                                                                                        100).release().context_click()
            actions.perform()
            time.sleep(2)

            menuVertical = self.driver.find_element(By.XPATH, '//div[@class = "workbench-menu-vertical"]')
            menuVertical.find_elements(By.CLASS_NAME, 'el-menu-item')[0].click()

            time.sleep(2)
            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[0].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            labelValue = {}
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False
                if isTextarea:
                    elInput = content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                else:
                    elInput = content.find_element(By.CSS_SELECTOR, '.el-input__inner')
                self.driver.execute_script("arguments[0].scrollIntoView(false);", elInput)
                elInput.clear()
                elInput.send_keys('测试新增' + label.replace(':', ''))
                labelValue[label] = '测试新增' + label.replace(':', '')
            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            confirmModal = self.driver.find_element(By.CLASS_NAME, 'el-message-box__btns')
            confirmModal.find_elements(By.TAG_NAME, 'span')[1].click()
            time.sleep(2)

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[0].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False
                if isTextarea:
                    elInput = content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                else:
                    elInput = content.find_element(By.CSS_SELECTOR, '.el-input__inner')
                self.driver.execute_script("arguments[0].scrollIntoView(false);", elInput)
                currentValue = elInput.get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试知识数据-->人物-->' + label.replace(':', '') + '表单编辑功能成功!')

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[0].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-edit').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False
                if isTextarea:
                    elInput = content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                else:
                    elInput = content.find_element(By.CSS_SELECTOR, '.el-input__inner')
                self.driver.execute_script("arguments[0].scrollIntoView(false);", elInput)
                elInput.clear()
                elInput.send_keys('测试编辑' + label.replace(':', ''))
                labelValue[label] = '测试编辑' + label.replace(':', '')
            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            time.sleep(2)

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[0].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False
                if isTextarea:
                    elInput = content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                else:
                    elInput = content.find_element(By.CSS_SELECTOR, '.el-input__inner')
                self.driver.execute_script("arguments[0].scrollIntoView(false);", elInput)
                currentValue = elInput.get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试知识数据-->人物-->' + label.replace(':', '') + '表单编辑功能成功!')

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[0].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-close').click()
            time.sleep(1)
            confirmModal = self.driver.find_element(By.CLASS_NAME, 'el-message-box__btns')
            confirmModal.find_elements(By.TAG_NAME, 'span')[1].click()
            time.sleep(2)
            try:
                message = self.driver.find_element(By.CLASS_NAME, 'el-message__content').text
            except Exception as e:
                message = ''
            self.assertEqual('删除成功！', message, '删除知识数据-->人物记录成功')
        except Exception as e:
            logging.exception(e)

    def test_config_knowledge_event(self):
        try:
            canvas = self.driver.find_elements(By.CLASS_NAME, 'files-page')[0]
            canvas.find_element(By.TAG_NAME, 'pre')
            actions = ActionChains(self.driver).move_to_element(canvas).click_and_hold().move_by_offset(100,
                                                                                                        100).release().context_click()
            actions.perform()
            time.sleep(2)
            menuVertical = self.driver.find_element(By.XPATH, '//div[@class = "workbench-menu-vertical"]')
            menuVertical.find_elements(By.CLASS_NAME, 'el-menu-item')[3].click()
            time.sleep(2)
            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[1].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            labelValue = {}
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
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
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
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
                    labelValue[label] = selectItem.find_element(By.TAG_NAME, 'span').text
                    time.sleep(1)
                elif isTextarea:
                    input = content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                    input.clear()
                    input.send_keys('测试新增' + label.replace(':', ''))
                    labelValue[label] = '测试新增' + label.replace(':', '')
                elif isInput:
                    input = content.find_element(By.CSS_SELECTOR, '.el-input__inner')
                    input.clear()
                    input.send_keys('测试新增' + label.replace(':', ''))
                    labelValue[label] = '测试新增' + label.replace(':', '')


            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            confirmModal = self.driver.find_element(By.CLASS_NAME, 'el-message-box__btns')
            confirmModal.find_elements(By.TAG_NAME, 'span')[1].click()
            time.sleep(2)

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[1].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False

                currentValue = ''
                if isTextarea:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-textarea__inner').get_attribute('value')
                else:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-input__inner').get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试知识数据-->事件-->' + label.replace(':', '') + '表单编辑功能成功!')

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[1].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-edit').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
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
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
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
                        selectOption[len(selectOption) - 1].find_elements(By.CSS_SELECTOR, '.el-select-dropdown__item')[
                            0]
                    selectItem.click()
                    labelValue[label] = selectItem.find_element(By.TAG_NAME, 'span').text
                    time.sleep(1)
                elif isTextarea:
                    input = content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                    input.clear()
                    input.send_keys('测试编辑' + label.replace(':', ''))
                    labelValue[label] = '测试编辑' + label.replace(':', '')
                elif isInput:
                    input = content.find_element(By.CSS_SELECTOR, '.el-input__inner')
                    input.clear()
                    input.send_keys('测试编辑' + label.replace(':', ''))
                    labelValue[label] = '测试编辑' + label.replace(':', '')

            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            time.sleep(2)

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[1].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False

                currentValue = ''
                if isTextarea:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-textarea__inner').get_attribute('value')
                else:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-input__inner').get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试知识数据-->事件-->' + label.replace(':', '') + '表单编辑功能成功!')

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[1].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-close').click()
            time.sleep(1)
            confirmModal = self.driver.find_element(By.CLASS_NAME, 'el-message-box__btns')
            confirmModal.find_elements(By.TAG_NAME, 'span')[1].click()
            time.sleep(2)
            try:
                message = self.driver.find_element(By.CLASS_NAME, 'el-message__content').text
            except Exception as e:
                message = ''
            self.assertEqual('删除成功！', message, '删除知识数据-->事件记录成功')
        except Exception as e:
            logging.exception(e)

    def test_config_knowledge_subject(self):
        try:
            canvas = self.driver.find_elements(By.CLASS_NAME, 'files-page')[0]
            canvas.find_element(By.TAG_NAME, 'pre')
            actions = ActionChains(self.driver).move_to_element(canvas).click_and_hold().move_by_offset(100,
                                                                                                        100).release().context_click()
            actions.perform()
            time.sleep(2)
            menuVertical = self.driver.find_element(By.XPATH, '//div[@class = "workbench-menu-vertical"]')
            menuVertical.find_elements(By.CLASS_NAME, 'el-menu-item')[2].click()
            time.sleep(2)
            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[2].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            labelValue = {}
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                elInput = content.find_element(By.CSS_SELECTOR, 'div:first-child')

                isInput = True
                try:
                    elInput.find_element(By.CLASS_NAME, 'el-input__inner')
                except Exception as e:
                    isInput = False

                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False
                if isTextarea:
                    input = content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                    input.clear()
                    input.send_keys('测试新增' + label.replace(':', ''))
                    labelValue[label] = '测试新增' + label.replace(':', '')
                elif isInput:
                    input = content.find_element(By.CSS_SELECTOR, '.el-input__inner')
                    input.clear()
                    input.send_keys('测试新增' + label.replace(':', ''))
                    labelValue[label] = '测试新增' + label.replace(':', '')


            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            time.sleep(2)

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[2].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False

                currentValue = ''
                if isTextarea:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-textarea__inner').get_attribute('value')
                else:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-input__inner').get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试知识数据-->专题-->' + label.replace(':', '') + '表单编辑功能成功!')

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[2].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-edit').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                elInput = content.find_element(By.CSS_SELECTOR, 'div:first-child')


                isInput = True
                try:
                    elInput.find_element(By.CLASS_NAME, 'el-input__inner')
                except Exception as e:
                    isInput = False

                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False

                if isTextarea:
                    input = content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                    input.clear()
                    input.send_keys('测试编辑' + label.replace(':', ''))
                    labelValue[label] = '测试编辑' + label.replace(':', '')
                elif isInput:
                    input = content.find_element(By.CSS_SELECTOR, '.el-input__inner')
                    input.clear()
                    input.send_keys('测试编辑' + label.replace(':', ''))
                    labelValue[label] = '测试编辑' + label.replace(':', '')

            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            time.sleep(2)

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[2].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False

                currentValue = ''
                if isTextarea:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-textarea__inner').get_attribute('value')
                else:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-input__inner').get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试知识数据-->专题-->' + label.replace(':', '') + '表单编辑功能成功!')

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[2].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-close').click()
            time.sleep(1)
            confirmModal = self.driver.find_element(By.CLASS_NAME, 'el-message-box__btns')
            confirmModal.find_elements(By.TAG_NAME, 'span')[1].click()
            time.sleep(2)
            try:
                message = self.driver.find_element(By.CLASS_NAME, 'el-message__content').text
            except Exception as e:
                message = ''
            self.assertEqual('删除成功！', message, '删除知识数据-->专题记录成功')
        except Exception as e:
            logging.exception(e)

    def test_config_knowledge_organization(self):
        try:
            canvas = self.driver.find_elements(By.CLASS_NAME, 'files-page')[0]
            canvas.find_element(By.TAG_NAME, 'pre')
            actions = ActionChains(self.driver).move_to_element(canvas).click_and_hold().move_by_offset(100,
                                                                                                        100).release().context_click()
            actions.perform()
            time.sleep(2)
            menuVertical = self.driver.find_element(By.XPATH, '//div[@class = "workbench-menu-vertical"]')
            menuVertical.find_elements(By.CLASS_NAME, 'el-menu-item')[3].click()
            time.sleep(2)
            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[3].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            labelValue = {}
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
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
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
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
                    labelValue[label] = selectItem.find_element(By.TAG_NAME, 'span').text
                    time.sleep(1)
                elif isTextarea:
                    input = content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                    input.clear()
                    input.send_keys('测试新增' + label.replace(':', ''))
                    labelValue[label] = '测试新增' + label.replace(':', '')
                elif isInput:
                    input = content.find_element(By.CSS_SELECTOR, '.el-input__inner')
                    input.clear()
                    input.send_keys('测试新增' + label.replace(':', ''))
                    labelValue[label] = '测试新增' + label.replace(':', '')


            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            confirmModal = self.driver.find_element(By.CLASS_NAME, 'el-message-box__btns')
            confirmModal.find_elements(By.TAG_NAME, 'span')[1].click()
            time.sleep(2)

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[3].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False

                currentValue = ''
                if isTextarea:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-textarea__inner').get_attribute('value')
                else:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-input__inner').get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试知识数据-->机构-->' + label.replace(':', '') + '表单编辑功能成功!')

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[3].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-edit').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
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
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
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
                        selectOption[len(selectOption) - 1].find_elements(By.CSS_SELECTOR, '.el-select-dropdown__item')[
                            0]
                    selectItem.click()
                    labelValue[label] = selectItem.find_element(By.TAG_NAME, 'span').text
                    time.sleep(1)
                elif isTextarea:
                    input = content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                    input.clear()
                    input.send_keys('测试编辑' + label.replace(':', ''))
                    labelValue[label] = '测试编辑' + label.replace(':', '')
                elif isInput:
                    input = content.find_element(By.CSS_SELECTOR, '.el-input__inner')
                    input.clear()
                    input.send_keys('测试编辑' + label.replace(':', ''))
                    labelValue[label] = '测试编辑' + label.replace(':', '')

            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            time.sleep(2)

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[3].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False

                currentValue = ''
                if isTextarea:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-textarea__inner').get_attribute('value')
                else:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-input__inner').get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试知识数据-->机构-->' + label.replace(':', '') + '表单编辑功能成功!')

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[3].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-close').click()
            time.sleep(1)
            confirmModal = self.driver.find_element(By.CLASS_NAME, 'el-message-box__btns')
            confirmModal.find_elements(By.TAG_NAME, 'span')[1].click()
            time.sleep(2)
            try:
                message = self.driver.find_element(By.CLASS_NAME, 'el-message__content').text
            except Exception as e:
                message = ''
            self.assertEqual('删除成功！', message, '删除知识数据-->机构记录成功')
        except Exception as e:
            logging.exception(e)

    def test_config_knowledge_geography(self):
        try:
            canvas = self.driver.find_elements(By.CLASS_NAME, 'files-page')[0]
            canvas.find_element(By.TAG_NAME, 'pre')
            actions = ActionChains(self.driver).move_to_element(canvas).click_and_hold().move_by_offset(100,
                                                                                                        100).release().context_click()
            actions.perform()
            time.sleep(2)
            menuVertical = self.driver.find_element(By.XPATH, '//div[@class = "workbench-menu-vertical"]')
            menuVertical.find_elements(By.CLASS_NAME, 'el-menu-item')[4].click()
            time.sleep(2)
            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[4].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            labelValue = {}
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                elInput = content.find_element(By.CSS_SELECTOR, 'div:first-child')

                isInput = True
                try:
                    elInput.find_element(By.CLASS_NAME, 'el-input__inner')
                except Exception as e:
                    isInput = False

                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False
                if isTextarea:
                    input = content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                    input.clear()
                    input.send_keys('测试新增' + label.replace(':', ''))
                    labelValue[label] = '测试新增' + label.replace(':', '')
                elif isInput:
                    input = content.find_element(By.CSS_SELECTOR, '.el-input__inner')
                    input.clear()
                    input.send_keys('测试新增' + label.replace(':', ''))
                    labelValue[label] = '测试新增' + label.replace(':', '')


            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            confirmModal = self.driver.find_element(By.CLASS_NAME, 'el-message-box__btns')
            confirmModal.find_elements(By.TAG_NAME, 'span')[1].click()
            time.sleep(2)

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[4].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False

                currentValue = ''
                if isTextarea:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-textarea__inner').get_attribute('value')
                else:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-input__inner').get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试知识数据-->地理名称-->' + label.replace(':', '') + '表单编辑功能成功!')

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[4].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-edit').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                elInput = content.find_element(By.CSS_SELECTOR, 'div:first-child')


                isInput = True
                try:
                    elInput.find_element(By.CLASS_NAME, 'el-input__inner')
                except Exception as e:
                    isInput = False

                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False

                if isTextarea:
                    input = content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                    input.clear()
                    input.send_keys('测试编辑' + label.replace(':', ''))
                    labelValue[label] = '测试编辑' + label.replace(':', '')
                elif isInput:
                    input = content.find_element(By.CSS_SELECTOR, '.el-input__inner')
                    input.clear()
                    input.send_keys('测试编辑' + label.replace(':', ''))
                    labelValue[label] = '测试编辑' + label.replace(':', '')

            saveButton = self.driver.find_element(By.XPATH, '//i[@class = "el-icon-document-add"]')
            self.driver.execute_script("arguments[0].scrollIntoView(false);", saveButton)
            saveButton.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//span[text()="同步"]').click()
            time.sleep(2)

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[4].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-arrow-down').click()
            time.sleep(1)
            for item in addFormSection.find_elements(By.CSS_SELECTOR, '.el-form-item.is-required'):
                label = item.find_element(By.CLASS_NAME, 'el-form-item__label').text
                content = item.find_element(By.CSS_SELECTOR, '.el-form-item__content')
                isTextarea = True
                try:
                    content.find_element(By.CSS_SELECTOR, '.el-textarea__inner')
                except Exception as e:
                    isTextarea = False

                currentValue = ''
                if isTextarea:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-textarea__inner').get_attribute('value')
                else:
                    currentValue = item.find_element(By.CLASS_NAME, 'el-input__inner').get_attribute('value')
                self.assertEqual(labelValue[label], currentValue,
                                 '测试知识数据-->地理名称-->' + label.replace(':', '') + '表单编辑功能成功!')

            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')
            formSectionList = formContainerList[4].find_elements(By.CLASS_NAME, 'form-section')
            addFormSection = formSectionList[len(formSectionList) - 1]
            addFormSection.find_element(By.CLASS_NAME, 'el-icon-close').click()
            time.sleep(1)
            confirmModal = self.driver.find_element(By.CLASS_NAME, 'el-message-box__btns')
            confirmModal.find_elements(By.TAG_NAME, 'span')[1].click()
            time.sleep(2)
            try:
                message = self.driver.find_element(By.CLASS_NAME, 'el-message__content').text
            except Exception as e:
                message = ''
            self.assertEqual('删除成功！', message, '删除知识数据-->地理名称记录成功')
        except Exception as e:
            logging.exception(e)

    def test_graininess_count(self):
        try:
            self.driver.find_element(By.ID, 'tab-knowledge').click()
            time.sleep(3)
            knowledge = self.driver.find_elements(By.XPATH, '//div[@class="workbench-content"]')[2]
            totalCount = self.driver.find_element(By.ID, 'tab-knowledge').text.replace('知识数据（', '').replace('）', '')
            personCount = self.driver.find_element(By.ID, 'tab-person').text.replace('人物 (', '').replace(')', '')
            eventCount = self.driver.find_element(By.ID, 'tab-event').text.replace('事件 (', '').replace(')', '')
            subjectCount = self.driver.find_element(By.ID, 'tab-subject').text.replace('专题 (', '').replace(')', '')
            organizationCount = self.driver.find_element(By.ID, 'tab-organization').text.replace('机构 (', '').replace(
                ')', '')
            geographyCount = self.driver.find_element(By.ID, 'tab-geography').text.replace('地理名称 (', '').replace(')',
                                                                                                                 '')
            formContainerList = knowledge.find_elements(By.CLASS_NAME, 'form-container')

            self.assertEqual(len(formContainerList[0].find_elements(By.CLASS_NAME, 'form-section')), int(personCount),
                             '知识数据人物计数校验成功')
            self.assertEqual(len(formContainerList[1].find_elements(By.CLASS_NAME, 'form-section')), int(eventCount),
                             '知识数据事件计数校验成功')
            self.assertEqual(len(formContainerList[2].find_elements(By.CLASS_NAME, 'form-section')), int(subjectCount),
                             '知识数据专题计数校验成功')
            self.assertEqual(len(formContainerList[3].find_elements(By.CLASS_NAME, 'form-section')),
                             int(organizationCount), '知识数据机构计数校验成功')
            self.assertEqual(len(formContainerList[4].find_elements(By.CLASS_NAME, 'form-section')),
                             int(geographyCount), '知识数据地理名称计数校验成功')

            self.assertEqual(
                int(personCount) + int(eventCount) + int(subjectCount) + int(organizationCount) + int(geographyCount),
                int(totalCount), '知识数据计数校验成功')

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
