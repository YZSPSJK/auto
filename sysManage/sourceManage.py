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

    def test_source_manage(self):
        try:
            self.driver.find_element(By.XPATH, '//span[text()="系统管理"]').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="资源管理"]').click()
            time.sleep(1)

            firstTreeNode = self.driver.find_element(By.CLASS_NAME, 'el-tree-node__label')
            firstTreeNode.click()
            firstTreeNodeText = firstTreeNode.text
            time.sleep(1)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            for row in el_rows:
                cols = row.find_elements(By.TAG_NAME, 'span')
                self.assertEqual(cols[2].text, firstTreeNodeText, '点击树节点查询结果符合要求')

            el_form_contents = self.driver.find_elements(By.XPATH, '//div[@class="el-form-item__content"]')
            sourceNameInput = el_form_contents[0].find_element(By.CLASS_NAME, 'el-input__inner')
            sourceTypeInput = el_form_contents[1].find_element(By.CLASS_NAME, 'el-input__inner')

            sourceNameInput.clear()
            sourceNameInput.send_keys('资源管理')
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            for row in el_rows:
                cols = row.find_elements(By.TAG_NAME, 'span')
                self.assertIn('资源管理', cols[0].text, '根据资源名称查询正确')
            sourceNameInput.clear()

            selfelectArrowArray = self.driver.find_elements(By.XPATH, '//span[@class="el-input__suffix-inner"]')
            selfelectArrowArray[0].click()
            time.sleep(1)
            sourceTypeOptionMenu = self.driver.find_element(By.XPATH,
                                                            '//li[@class="el-select-dropdown__item"]/span[text()="菜单"]')
            sourceTypeOptionMenu.click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            for row in el_rows:
                cols = row.find_elements(By.TAG_NAME, 'span')
                self.assertIn('菜单', cols[1].text, '根据资源类型查询正确')

            sourceNameInput.clear()
            sourceNameInput.send_keys('资源管理')
            self.driver.find_element(By.XPATH, '//span[text()="重置"]').click()
            self.assertEqual(sourceNameInput.get_attribute('value'), '', '重置功能正确')
            self.assertEqual(sourceTypeInput.get_attribute('value'), '', '重置功能正确')

            self.driver.find_element(By.XPATH, '//span[text()="新建"]').click()
            time.sleep(1)
            dialog = self.driver.find_element(By.XPATH, '//div[@class="el-dialog" and @aria-label="新增资源"]')
            dialogBody = dialog.find_element(By.XPATH, '//div[@class="el-dialog__body"]')
            formInputs = dialogBody.find_elements(By.XPATH, '//input[@class="el-input__inner"]')
            timestamp = int(time.time())
            formInputs[4].send_keys('资源名称-测试' + str(timestamp))
            formInputs[7].send_keys(timestamp)
            formInputs[9].send_keys('/system')

            formInputs[5].click()
            time.sleep(1)
            sourceTypeMenu = self.driver.find_element(By.XPATH,
                                                      '//li[@class="el-select-dropdown__item"]/span[text()="菜单"]')
            sourceTypeMenu.click()
            time.sleep(1)
            formInputs[8].click()
            time.sleep(1)
            accessLevelAuth = self.driver.find_element(By.XPATH,
                                                       '//li[@class="el-select-dropdown__item"]/span[text()="授权访问"]')
            accessLevelAuth.click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, '.el-dropdown-selfdefine > span').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//ul/div/div[2]/div/span').click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR,
                                     '.el-dialog__footer:nth-child(3) .el-button--primary > span').click()

            time.sleep(2)
            sourceNameInput.clear()
            sourceNameInput.send_keys('资源名称-测试' + str(timestamp))
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            self.assertEqual(1, len(el_rows), '根据新增参数查询记录为一条')
            cols = el_rows[0].find_elements(By.TAG_NAME, 'span')
            self.assertEqual('资源名称-测试' + str(timestamp), cols[0].text, '新增和查询记录的资源名称相同')
            self.assertEqual('菜单', cols[1].text, '新增和查询记录的资源类型相同')
            self.assertEqual(firstTreeNodeText, cols[2].text, '新增和查询记录的上级资源相同')
            self.assertEqual('/system/*', cols[3].text, '新增和查询记录的ANT匹配格式相同')
            self.assertEqual('/system', cols[4].text, '新增和查询记录的访问路径相同')
            self.assertEqual('授权访问', cols[5].text, '新增和查询记录的访问控制级别相同')
            self.assertEqual(str(timestamp), cols[6].text, '新增和查询记录的优先级相同')

            self.driver.find_element(By.XPATH, '//span[text()="编辑"]').click()
            time.sleep(1)
            dialog = self.driver.find_element(By.XPATH, '//div[@class="el-dialog" and @aria-label="编辑资源"]')
            dialogBody = dialog.find_element(By.XPATH, '//div[@class="el-dialog__body"]')
            formInputs = dialogBody.find_elements(By.XPATH, '//input[@class="el-input__inner"]')
            formInputs[10].clear()
            formInputs[13].clear()
            formInputs[15].clear()
            formInputs[10].send_keys('资源名称-测试编辑' + str(timestamp))
            formInputs[13].send_keys(timestamp + 1)
            formInputs[15].send_keys('/system/update')

            formInputs[11].click()
            time.sleep(1)
            sourceTypeInterface = self.driver.find_elements(By.XPATH,
                                                            '//li[@class="el-select-dropdown__item"]/span[text()="接口"]')[
                2]
            sourceTypeInterface.click()
            time.sleep(1)
            formInputs[14].click()
            time.sleep(1)
            accessLevelApprove = self.driver.find_elements(By.XPATH,
                                                           '//li[@class="el-select-dropdown__item"]/span[text()="认证访问"]')[
                1]
            accessLevelApprove.click()
            time.sleep(1)

            saveButton = self.driver.find_elements(By.CSS_SELECTOR,
                                                   '.el-dialog__footer:nth-child(3) .el-button--primary > span')
            saveButton[1].click()
            time.sleep(2)
            sourceNameInput.clear()
            sourceNameInput.send_keys('资源名称-测试编辑' + str(timestamp))
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            cols = el_rows[0].find_elements(By.TAG_NAME, 'span')
            self.assertEqual('资源名称-测试编辑' + str(timestamp), cols[0].text, '编辑和查询记录的资源名称相同')
            self.assertEqual('接口', cols[1].text, '编辑和查询记录的资源类型相同')
            self.assertEqual(firstTreeNodeText, cols[2].text, '编辑和查询记录的上级资源相同')
            self.assertEqual('/system/update', cols[3].text, '编辑和查询记录的ANT匹配格式相同')
            self.assertEqual('/system/update', cols[4].text, '编辑和查询记录的访问路径相同')
            self.assertEqual('认证访问', cols[5].text, '编辑和查询记录的访问控制级别相同')
            self.assertEqual(str(timestamp + 1), cols[6].text, '编辑和查询记录的优先级相同')

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
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestCase))
    br = BeautifulReport(suite)
    br.report(filename='sourceManage.html', description='测试报告',
              report_dir='/Users/sjk/workspace/sjk/python/auto/testReport')
