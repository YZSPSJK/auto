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
        self.driver.get('http://146.56.203.127:8143/library-test/home')
        self.driver.add_cookie(
            {'domain': '146.56.203.127', 'httpOnly': False, 'name': 'library_admin_token', 'path': '/', 'secure': False,
             'value': 'Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiMTAwMyJdLCJ1c2VyX25hbWUiOiJ0ZXN0dXNlciIsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJleHAiOjE2NzkwNjI3NjksImF1dGhvcml0aWVzIjpbIlJPTEVfUk9MRTAwMSIsIlJPTEVfQURNSU4iXSwianRpIjoiMzE1OWQwYjEtNDBjNy00MDliLTgwNWMtZDc4MTRjN2Q0ZjUyIiwiY2xpZW50X2lkIjoibWVzc2FnaW5nLWNsaWVudCIsImFkZGl0aW9uIjpudWxsfQ.OU1kgjeKnQwsKfqw9X7R-JNzGrGwZrhROhzvwGFsVqgI6lsEvZ2pvHPQm6KR8uscmNIkqqi6z9QTw7sVGdPrEPG2VSwnofgZJk7D8071ou4v-4V76oj36nZmSjnypnb4rI6cwU5yNMOIxlZUYhSciKCN_8UbW5MIRaRnt_U3ckQCXge4xYKLTf_ryYBGGhoqqO7ETnD-fitifuh-wHoIdMvKs0M2ZateZFjfsg8kQWUOHBoGvHH54ak_NwwAEipTixTEaouTzDEtfxyTStxcICA50D5ZQstMyRVU3yksvLje-7Gazqcu6Lo2QcHt4iBAw6KXoiiX9fQWu4bvDw_kBg'})
        self.driver.refresh()
        time.sleep(2)
        self.driver.get('http://146.56.203.127:8143/library-test/workbench/180010020230000068')
        time.sleep(2)

    def test_account_manage(self):
        try:

            # self.driver.find_element(By.XPATH, '//i[contains(@class, "el-icon-user")]').click()
            # time.sleep(1)
            # self.driver.find_element(By.XPATH, '//span[text()="资源列表"]').click()
            # time.sleep(2)
            # el_form_contents = self.driver.find_elements(By.XPATH, '//div[@class="el-form-item__content"]')
            #
            # jobName = el_form_contents[0].find_element(By.CLASS_NAME, 'el-input__inner')
            # jobStatus = el_form_contents[1].find_element(By.CLASS_NAME, 'el-input__inner')
            # jobStatus.click()
            # time.sleep(1)
            # jobStatusFinish = self.driver.find_element(By.XPATH,
            #                                                '//li[@class="el-select-dropdown__item"]/span[text()="加工完成"]')
            #
            # jobStatusFinish.click()
            # time.sleep(1)
            #
            # jobName.clear()
            # jobName.send_keys('测试')
            # self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            # time.sleep(2)
            # el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            # for row in el_rows:
            #     cols = row.find_elements(By.CLASS_NAME, 'cell')
            #     if cols[1].text.lower() == '180010020230000069':
            #         row.find_element(By.XPATH, '//span[text()="抽取"]').click()
            # time.sleep(3)

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

            #
            # self.driver.find_element(By.XPATH, '//span[text()="新增账户"]').click()
            # time.sleep(1)
            # dialog = self.driver.find_element(By.XPATH, '//div[@class="el-dialog" and @aria-label="新增账户"]')
            # dialogBody = dialog.find_element(By.XPATH, '//div[@class="el-dialog__body"]')
            # formInputs = dialogBody.find_elements(By.XPATH, '//input[@class="el-input__inner"]')
            # timestamp = int(time.time())
            # formInputs[7].send_keys('客户名称-测试' + str(timestamp))
            # formInputs[8].send_keys('显示名称-测试' + str(timestamp))
            # formInputs[9].click()
            # time.sleep(1)
            # firstOrgTreeNode = self.driver.find_elements(By.XPATH,
            #                                              '//li[contains(@class, "el-select-dropdown__item")]//span[contains(text(), "测试部门5") and @class="el-tree-node__label"]')[
            #     1]
            #
            # firstOrgTreeNode.click()
            # formInputs[10].click()
            # time.sleep(1)
            # firstAccountStatusTreeNode = self.driver.find_elements(By.XPATH,
            #                                                        '//li[contains(@class, "el-select-dropdown__item")]//span[text()="激活状态"]')[
            #     1]
            #
            # firstAccountStatusTreeNode.click()
            #
            # formInputs[11].click()
            # time.sleep(1)
            # firstRoleTreeNode = self.driver.find_elements(By.XPATH,
            #                                               '//li[contains(@class, "el-select-dropdown__item")]//span[text()="管理员"]')[
            #     1]
            #
            # firstRoleTreeNode.click()
            # time.sleep(1)
            # self.driver.find_element(By.CSS_SELECTOR,
            #                          '.el-dialog__footer:nth-child(3) .el-button--primary > span').click()
            # time.sleep(2)
            # accountName.clear()
            # accountFullName.clear()
            # accountName.send_keys('客户名称-测试' + str(timestamp))
            # accountFullName.send_keys('显示名称-测试' + str(timestamp))
            # self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            # time.sleep(2)
            # el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            # self.assertEqual(1, len(el_rows), '根据新增参数查询记录为一条')
            # cols = el_rows[0].find_elements(By.TAG_NAME, 'span')
            # self.assertEqual('客户名称-测试' + str(timestamp), cols[0].text, '新增和查询记录的客户名称相同')
            # self.assertEqual('显示名称-测试' + str(timestamp), cols[1].text, '新增和查询记录的显示名称相同')
            # self.assertIn('测试部门5', cols[2].text, '新增和查询记录的所属机构相同')
            # self.assertIn('管理员', cols[3].text, '新增和查询记录的所属角色相同')
            # self.assertEqual('激活状态', cols[5].text, '新增和查询记录的账户状态相同')
            #
            # self.driver.find_element(By.XPATH, '//span[text()="编辑"]').click()
            # time.sleep(1)
            # dialog = self.driver.find_element(By.XPATH, '//div[@class="el-dialog" and @aria-label="编辑账户"]')
            # dialogBody = dialog.find_element(By.XPATH, '//div[@class="el-dialog__body"]')
            # formInputs = dialogBody.find_elements(By.XPATH, '//input[@class="el-input__inner"]')
            #
            # formInputs[13].clear()
            # formInputs[13].send_keys('显示名称-测试编辑' + str(timestamp))
            #
            # formInputs[14].click()
            # time.sleep(1)
            # firstOrgTreeNode = self.driver.find_elements(By.XPATH,
            #                                              '//li[contains(@class, "el-select-dropdown__item")]//span[contains(text(), "测试部门4") and @class="el-tree-node__label"]')[
            #     2]
            # firstOrgTreeNode.click()
            # formInputs[15].click()
            # time.sleep(1)
            # firstAccountStatusTreeNode = self.driver.find_elements(By.XPATH,
            #                                                        '//li[contains(@class, "el-select-dropdown__item")]//span[text()="锁定状态"]')[
            #     2]
            # firstAccountStatusTreeNode.click()
            #
            # self.driver.find_elements(By.XPATH, '//span[@class="el-input__suffix-inner"]')[9].click()
            # time.sleep(1)
            #
            # firstRoleTreeNode = self.driver.find_elements(By.XPATH,
            #                                               '//li[contains(@class, "el-select-dropdown__item")]//span[text()="hhhhhh"]')[
            #     2]
            # firstRoleTreeNode.click()
            # time.sleep(1)
            # saveButton = self.driver.find_elements(By.CSS_SELECTOR,
            #                                        '.el-dialog__footer:nth-child(3) .el-button--primary > span')
            # saveButton[1].click()
            # time.sleep(2)
            # accountName.clear()
            # accountFullName.clear()
            # accountName.send_keys('客户名称-测试' + str(timestamp))
            # accountFullName.send_keys('显示名称-测试编辑' + str(timestamp))
            # self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            # time.sleep(2)
            # el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            # cols = el_rows[0].find_elements(By.TAG_NAME, 'span')
            # self.assertEqual('客户名称-测试' + str(timestamp), cols[0].text, '编辑和查询记录的客户名称相同')
            # self.assertEqual('显示名称-测试编辑' + str(timestamp), cols[1].text, '编辑和查询记录的显示名称相同')
            # self.assertIn('测试部门4', cols[2].text, '编辑和查询记录的所属机构相同')
            # self.assertIn('hhhhhh', cols[3].text, '编辑和查询记录的所属角色相同')
            # self.assertEqual('锁定状态', cols[5].text, '编辑和查询记录的账户状态相同')
            #
            # self.driver.find_element(By.XPATH, '//span[text()="冻结"]').click()
            # time.sleep(1)
            # self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            # time.sleep(2)
            # el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            # cols = el_rows[0].find_elements(By.TAG_NAME, 'span')
            # self.assertEqual('注销状态', cols[5].text, '冻结功能正常')
            #
            # self.driver.find_element(By.XPATH, '//span[text()="删除"]').click()
            # time.sleep(1)
            # self.driver.find_element(By.CSS_SELECTOR, '.el-button--default:nth-child(2) > span:nth-child(1)').click()
            # time.sleep(1)
            # el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            # self.assertEqual(0, len(el_rows), '根据参数,删除按钮点击后查询记录为0')

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
