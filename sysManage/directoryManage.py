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
        self.driver.add_cookie(
            {'domain': '175.27.232.12', 'httpOnly': False, 'name': 'skyrim_admin_token', 'path': '/', 'secure': False,
             'value': 'Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiMTAwMyJdLCJ1c2VyX25hbWUiOiJ1c2VyMSIsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJleHAiOjE2NTg5MDM3NTcsImF1dGhvcml0aWVzIjpbIlJPTEVfQURNSU4iXSwianRpIjoiMjFhMjU3ZWMtNjk3ZC00OTdiLTg2MDEtYmZjNDhmYjI3ZjhhIiwiY2xpZW50X2lkIjoibWVzc2FnaW5nLWNsaWVudCJ9.UHtKM_9lG3b1xNoGkjicVM4kJDMdQxxU-2z4-Le0scKtSTfLLK4byV2xvCmaD7Legmd1f9XqgPK9eoOHL798MR0Gv3gwZFDWLRakiOfha2CfDh0HJQTJr5EvxB7NNkFYgf9tiuV2vtI-0vVGNmMyo5oOG1wIHYVptEPuj402-nPCz0gM_VFW4v5Pcn1jKu8JQEREYcQpn8UnBzGCopa7Iap1fykRMkItYlawa21E6PuGYGDS_YMAd5pczpif6L3kk0RTUpddqxJUY9gF9cmz3I7p5SKavZvLceXKyWqcoeuNt7GmD1CiZ-UVXf8tTenReweOiA8GK6D17KrEib0Lyg'})
        self.driver.refresh()
        time.sleep(1)

    def test_directory_manage(self):
        try:
            self.driver.find_element(By.XPATH, '//span[text()="系统管理"]').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="字典管理"]').click()
            self.driver.find_elements()
            time.sleep(1)
            el_form_contents = self.driver.find_elements(By.XPATH, '//div[@class="el-form-item__content"]')
            directoryCode = el_form_contents[0].find_element(By.CLASS_NAME, 'el-input__inner')
            directoryName = el_form_contents[1].find_element(By.CLASS_NAME, 'el-input__inner')
            isModifyInput = el_form_contents[2].find_element(By.CLASS_NAME, 'el-input__inner')

            time.sleep(1)
            directoryCode.clear()
            directoryCode.send_keys('RESOURCE_TYPE')
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            for row in el_rows:
                cols = row.find_elements(By.TAG_NAME, 'span')
                self.assertIn('RESOURCE_TYPE', cols[0].text, '根据字典编号查询正确')

            directoryCode.clear()
            directoryName.clear()
            directoryName.send_keys('资源类别')
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            for row in el_rows:
                cols = row.find_elements(By.TAG_NAME, 'span')
                self.assertIn('资源类别', cols[1].text, '根据字典名称查询正确')

            directoryCode.clear()
            directoryName.clear()
            isModifySelectArrowArray = self.driver.find_elements(By.XPATH, '//span[@class="el-input__suffix-inner"]')
            isModifySelectArrowArray[0].click()
            time.sleep(1)
            isModifyOptionYes = self.driver.find_element(By.XPATH,
                                                         '//li[@class="el-select-dropdown__item"]/span[text()="是"]')
            isModifyOptionYes.click()
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            for row in el_rows:
                cols = row.find_elements(By.TAG_NAME, 'span')
                self.assertEqual('是', cols[3].text, '根据是否编辑查询正确')

            directoryCode.clear()
            directoryName.clear()
            directoryCode.send_keys('RESOURCE_TYPE')
            directoryName.send_keys('资源类别')
            isModifySelectArrowArray = self.driver.find_elements(By.XPATH, '//span[@class="el-input__suffix-inner"]')
            isModifySelectArrowArray[0].click()
            time.sleep(2)
            isModifyOptionNo = self.driver.find_element(By.XPATH,
                                                        '//li[@class="el-select-dropdown__item"]/span[text()="否"]')
            isModifyOptionNo.click()
            self.driver.find_element(By.XPATH, '//span[text()="重置"]').click()
            self.assertEqual(directoryCode.get_attribute('value'), '', '重置功能正确')
            self.assertEqual(directoryName.get_attribute('value'), '', '重置功能正确')
            self.assertEqual(isModifyInput.get_attribute('value'), '', '重置功能正确')

            self.driver.find_element(By.XPATH, '//span[text()="新增字典"]').click()
            time.sleep(1)
            dialog = self.driver.find_element(By.XPATH, '//div[@class="el-dialog" and @aria-label="新增字典"]')
            dialogBody = dialog.find_element(By.XPATH, '//div[@class="el-dialog__body"]')
            formInputs = dialogBody.find_elements(By.XPATH, '//input[@class="el-input__inner"]')
            timestamp = int(time.time())
            formInputs[5].send_keys('字典编号-测试' + str(timestamp))
            formInputs[6].send_keys('字典名称-测试' + str(timestamp))
            formInputs[7].send_keys(timestamp)
            self.driver.find_element(By.CSS_SELECTOR,
                                     '.el-dialog__footer:nth-child(3) .el-button--primary > span').click()

            time.sleep(2)
            directoryCode.clear()
            directoryName.clear()
            directoryCode.send_keys('字典编号-测试' + str(timestamp))
            directoryName.send_keys('字典名称-测试' + str(timestamp))
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            self.assertEqual(1, len(el_rows), '根据新增参数查询记录为一条')
            cols = el_rows[0].find_elements(By.TAG_NAME, 'span')
            self.assertEqual('字典编号-测试' + str(timestamp), cols[0].text, '新增和查询记录的字典编号相同')
            self.assertEqual('字典名称-测试' + str(timestamp), cols[1].text, '新增和查询记录的字典名称相同')
            self.assertEqual(str(timestamp), cols[2].text, '新增和查询记录的排序相同')
            self.assertEqual('是', cols[3].text, '新增和查询记录的是否编辑相同')

            self.driver.find_element(By.XPATH, '//span[text()="编辑"]').click()
            time.sleep(1)
            dialog = self.driver.find_element(By.XPATH, '//div[@class="el-dialog" and @aria-label="编辑字典"]')
            dialogBody = dialog.find_element(By.XPATH, '//div[@class="el-dialog__body"]')
            formInputs = dialogBody.find_elements(By.XPATH, '//input[@class="el-input__inner"]')
            formInputs[9].clear()
            formInputs[9].send_keys('字典名称-测试编辑' + str(timestamp))

            formInputs[10].clear()
            formInputs[10].send_keys(timestamp + 1)
            saveButton = self.driver.find_elements(By.CSS_SELECTOR,
                                                   '.el-dialog__footer:nth-child(3) .el-button--primary > span')
            saveButton[1].click()
            time.sleep(2)
            directoryName.clear()
            directoryName.send_keys('字典名称-测试编辑' + str(timestamp))
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            cols = el_rows[0].find_elements(By.TAG_NAME, 'span')
            self.assertEqual('字典名称-测试编辑' + str(timestamp), cols[1].text, '编辑功能正常')
            self.assertEqual(str(timestamp + 1), cols[2].text, '编辑功能正常')

            # 字典配置功能
            self.driver.find_element(By.XPATH, '//span[text()="字典配置"]').click()
            time.sleep(1)
            dialog = self.driver.find_element(By.XPATH, '//div[@class="el-dialog" and @aria-label="字典配置"]')
            dialog.find_element(By.XPATH, '//span[text()="新增子项"]').click()
            dialogBody = dialog.find_element(By.XPATH, '//div[@class="el-dialog__body"]')
            formInputs = dialogBody.find_elements(By.XPATH, '//input[@class="el-input__inner"]')
            formInputs[11].send_keys('1')
            formInputs[12].send_keys('2')
            formInputs[13].send_keys('3')
            formInputs[14].send_keys('4')
            saveButton = self.driver.find_elements(By.CSS_SELECTOR,
                                                   '.el-dialog__footer:nth-child(3) .el-button--primary > span')
            saveButton[2].click()
            time.sleep(1)
            childrenTableData = dialogBody.find_elements(By.XPATH,
                                                         '//div[@class="el-dialog__body"]//tr[@class="el-table__row"]')
            for row in childrenTableData:
                cols = row.find_elements(By.TAG_NAME, 'span')
                self.assertEqual('字典编号-测试' + str(timestamp), cols[0].text, '新增字典子项, 字典标签和字典项的字典编号一致')
                self.assertEqual('1', cols[1].text, '新增字典子项, 字典编号一致')
                self.assertEqual('2', cols[2].text, '新增字典子项, 字典键值一致')
                self.assertEqual('3', cols[3].text, '新增字典子项, 字典键值英文一致')
                self.assertEqual('4', cols[4].text, '新增字典子项, 字典排序一致')

            dialog.find_element(By.XPATH, '//span[text()="新增子项"]').click()
            formInputs[11].send_keys('1')
            formInputs[12].send_keys('2')
            formInputs[13].send_keys('3')
            formInputs[14].send_keys('4')
            saveButton = self.driver.find_elements(By.CSS_SELECTOR,
                                                   '.el-dialog__footer:nth-child(3) .el-button--primary > span')
            saveButton[2].click()
            time.sleep(2)
            try:
                message = self.driver.find_element(By.CLASS_NAME, 'el-message__content').text
            except Exception as e:
                message = ''
            self.assertEqual('字典编号不能重复', message, '新增字典子项, 字典编号不能重复')
            formInputs[11].click()
            formInputs[11].clear()
            formInputs[11].send_keys('4')
            saveButton = self.driver.find_elements(By.CSS_SELECTOR,
                                                   '.el-dialog__footer:nth-child(3) .el-button--primary > span')
            saveButton[2].click()
            time.sleep(2)
            try:
                message = self.driver.find_elements(By.CLASS_NAME, 'el-message__content')[1].text
            except Exception as e:
                message = ''
            self.assertEqual('排序不能重复!', message, '新增字典子项, 字典排序不能重复')
            formInputs[14].clear()
            formInputs[14].send_keys('1')
            saveButton = self.driver.find_elements(By.CSS_SELECTOR,
                                                   '.el-dialog__footer:nth-child(3) .el-button--primary > span')
            saveButton[2].click()
            time.sleep(1)
            childrenTableData = dialogBody.find_elements(By.XPATH,
                                                         '//div[@class="el-dialog__body"]//tr[@class="el-table__row"]')
            cols = childrenTableData[1].find_elements(By.TAG_NAME, 'span')
            self.assertEqual('字典编号-测试' + str(timestamp), cols[0].text, '新增字典子项, 字典标签和字典项的字典编号一致')
            self.assertEqual('4', cols[1].text, '新增字典子项, 字典编号一致')
            self.assertEqual('2', cols[2].text, '新增字典子项, 字典键值一致')
            self.assertEqual('3', cols[3].text, '新增字典子项, 字典键值英文一致')
            self.assertEqual('1', cols[4].text, '新增字典子项, 字典排序一致')
            time.sleep(2)

            deleteButtonArray = dialogBody.find_elements(By.XPATH,
                                                         '//div[@class="el-dialog__body"]//tr[@class="el-table__row"]//span[text()="删除"]')
            deleteButtonArray[1].click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, '.el-button--default:nth-child(2) > span:nth-child(1)').click()
            time.sleep(2)
            try:
                message = self.driver.find_element(By.CLASS_NAME, 'el-message__content').text
            except Exception as e:
                message = ''
            self.assertEqual('删除成功!', message, '删除字典子项1成功')
            time.sleep(1)
            childrenTableData = dialogBody.find_elements(By.XPATH,
                                                         '//div[@class="el-dialog__body"]//tr[@class="el-table__row"]')
            self.assertEqual(1, len(childrenTableData), '删除字典子项成功后,子项记录为1')
            self.driver.find_element(By.CSS_SELECTOR, '.el-dialog__wrapper:nth-child(8) .el-dialog__close').click()
            time.sleep(1)

            self.driver.find_element(By.XPATH, '//span[text()="删除"]').click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, '.el-button--default:nth-child(2) > span:nth-child(1)').click()
            time.sleep(1)
            try:
                message = self.driver.find_element(By.CLASS_NAME, 'el-message__content').text
            except Exception as e:
                message = ''
            self.assertEqual('有未删除的字典值', message, '存在字典子项无法删除字典项本身')

            self.driver.find_element(By.XPATH, '//span[text()="字典配置"]').click()
            time.sleep(1)

            dialogBody.find_element(By.XPATH,
                                    '//div[@class="el-dialog__body"]//tr[@class="el-table__row"]//span[text()="编辑"]').click()
            formInputs = dialogBody.find_elements(By.XPATH, '//input[@class="el-input__inner"]')
            formInputs[15].clear()
            formInputs[15].send_keys('11')
            formInputs[16].clear()
            formInputs[16].send_keys('22')
            formInputs[17].clear()
            formInputs[17].send_keys('33')
            formInputs[18].clear()
            formInputs[18].send_keys('44')
            saveButton = self.driver.find_elements(By.CSS_SELECTOR,
                                                   '.el-dialog__footer:nth-child(3) .el-button--primary > span')
            saveButton[3].click()
            time.sleep(1)
            childrenTableData = dialogBody.find_elements(By.XPATH,
                                                         '//div[@class="el-dialog__body"]//tr[@class="el-table__row"]')
            for row in childrenTableData:
                cols = row.find_elements(By.TAG_NAME, 'span')
                self.assertEqual('字典编号-测试' + str(timestamp), cols[0].text, '编辑字典子项, 字典标签和字典项的字典编号一致')
                self.assertEqual('11', cols[1].text, '编辑字典子项, 字典编号一致')
                self.assertEqual('22', cols[2].text, '编辑字典子项, 字典键值一致')
                self.assertEqual('33', cols[3].text, '编辑字典子项, 字典键值英文一致')
                self.assertEqual('44', cols[4].text, '编辑字典子项, 字典排序一致')

            dialogBody.find_element(By.XPATH,
                                    '//div[@class="el-dialog__body"]//tr[@class="el-table__row"]//span[text()="删除"]').click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, '.el-button--default:nth-child(2) > span:nth-child(1)').click()
            time.sleep(2)
            try:
                message = self.driver.find_element(By.CLASS_NAME, 'el-message__content').text
            except Exception as e:
                message = ''
            self.assertEqual('删除成功!', message, '删除字典子项2成功')
            time.sleep(1)
            childrenTableData = dialogBody.find_elements(By.XPATH,
                                                         '//div[@class="el-dialog__body"]//tr[@class="el-table__row"]')
            self.assertEqual(0, len(childrenTableData), '删除字典子项成功后,子项记录为0')
            self.driver.find_element(By.CSS_SELECTOR, '.el-dialog__wrapper:nth-child(8) .el-dialog__close').click()
            time.sleep(1)

            self.driver.find_element(By.XPATH, '//span[text()="删除"]').click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, '.el-button--default:nth-child(2) > span:nth-child(1)').click()
            time.sleep(1)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            self.assertEqual(0, len(el_rows), '根据新增参数,删除按钮点击后查询记录为0')

        except Exception as e:
            logging.exception(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
