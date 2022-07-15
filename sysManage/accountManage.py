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

    def test_role_manage(self):
        try:
            self.driver.find_element(By.XPATH, '//span[text()="系统管理"]').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="账户管理"]').click()
            time.sleep(1)

            el_form_contents = self.driver.find_elements(By.XPATH, '//div[@class="el-form-item__content"]')
            accountName = el_form_contents[0].find_element(By.CLASS_NAME, 'el-input__inner')
            accountFullName = el_form_contents[1].find_element(By.CLASS_NAME, 'el-input__inner')
            accountStatus = el_form_contents[2].find_element(By.CLASS_NAME, 'el-input__inner')
            accountOrg = el_form_contents[3].find_element(By.CLASS_NAME, 'el-input__inner')
            accountRole = el_form_contents[4].find_element(By.CLASS_NAME, 'el-input__inner')

            accountName.clear()
            accountName.send_keys('测试')
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            for row in el_rows:
                cols = row.find_elements(By.TAG_NAME, 'span')
                self.assertIn('测试', cols[0].text.lower(), '根据账户名称查询正确')

            accountName.clear()
            accountFullName.clear()
            accountFullName.send_keys('测试')
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            for row in el_rows:
                cols = row.find_elements(By.TAG_NAME, 'span')
                self.assertIn('测试', cols[1].text.lower(), '根据账户全称查询正确')

            accountName.clear()
            accountFullName.clear()
            iconArrowUpArray = self.driver.find_elements(By.XPATH, '//span[@class="el-input__suffix-inner"]')
            iconArrowUpArray[0].click()
            time.sleep(1)
            accountStatusActive = self.driver.find_element(By.XPATH,
                                                           '//li[@class="el-select-dropdown__item"]/span[text()="激活状态"]')
            accountStatusActive.click()
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            for row in el_rows:
                cols = row.find_elements(By.TAG_NAME, 'span')
                self.assertEqual('激活状态', cols[5].text.lower(), '根据账户状态查询正确')

            iconArrowUpArray[1].click()
            time.sleep(1)
            firstOrgTreeNode = self.driver.find_elements(By.XPATH,
                                                         '//li[contains(@class, "el-select-dropdown__item")]//span[contains(text(), "测试") and @class="el-tree-node__label"]')[
                0]
            firstOrgTreeNode.click()
            firstOrgTreeNodeText = firstOrgTreeNode.text
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            for row in el_rows:
                cols = row.find_elements(By.TAG_NAME, 'span')
                self.assertEqual(firstOrgTreeNodeText, cols[2].text, '根据账户所属组织查询正确')

            iconArrowUpArray[2].click()
            time.sleep(1)
            manageRoleNode = self.driver.find_element(By.XPATH,
                                                      '//li[@class="el-select-dropdown__item"]/span[text()="管理员"]')
            manageRoleNode.click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            for row in el_rows:
                cols = row.find_elements(By.TAG_NAME, 'span')
                self.assertEqual('管理员', cols[3].text, '根据账户所属角色查询正确')

            self.driver.find_element(By.XPATH, '//span[text()="重置"]').click()
            self.assertEqual(accountName.get_attribute('value'), '', '重置功能正确')
            self.assertEqual(accountFullName.get_attribute('value'), '', '重置功能正确')
            self.assertEqual(accountStatus.get_attribute('value'), '', '重置功能正确')
            self.assertEqual(accountOrg.get_attribute('value'), '', '重置功能正确')
            self.assertEqual(accountRole.get_attribute('value'), '', '重置功能正确')

            self.driver.find_element(By.XPATH, '//span[text()="新增账户"]').click()
            time.sleep(1)
            dialog = self.driver.find_element(By.XPATH, '//div[@class="el-dialog" and @aria-label="新增账户"]')
            dialogBody = dialog.find_element(By.XPATH, '//div[@class="el-dialog__body"]')
            formInputs = dialogBody.find_elements(By.XPATH, '//input[@class="el-input__inner"]')
            timestamp = int(time.time())
            formInputs[7].send_keys('客户名称-测试' + str(timestamp))
            formInputs[8].send_keys('显示名称-测试' + str(timestamp))
            formInputs[9].click()
            time.sleep(1)
            firstOrgTreeNode = self.driver.find_elements(By.XPATH,
                                                         '//li[contains(@class, "el-select-dropdown__item")]//span[contains(text(), "测试部门5") and @class="el-tree-node__label"]')[
                1]

            firstOrgTreeNode.click()
            formInputs[10].click()
            time.sleep(1)
            firstAccountStatusTreeNode = self.driver.find_elements(By.XPATH,
                                                                   '//li[contains(@class, "el-select-dropdown__item")]//span[text()="激活状态"]')[
                1]

            firstAccountStatusTreeNode.click()

            formInputs[11].click()
            time.sleep(1)
            firstRoleTreeNode = self.driver.find_elements(By.XPATH,
                                                          '//li[contains(@class, "el-select-dropdown__item")]//span[text()="管理员"]')[
                1]

            firstRoleTreeNode.click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR,
                                     '.el-dialog__footer:nth-child(3) .el-button--primary > span').click()
            time.sleep(2)
            accountName.clear()
            accountFullName.clear()
            accountName.send_keys('客户名称-测试' + str(timestamp))
            accountFullName.send_keys('显示名称-测试' + str(timestamp))
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            self.assertEqual(1, len(el_rows), '根据新增参数查询记录为一条')
            cols = el_rows[0].find_elements(By.TAG_NAME, 'span')
            self.assertEqual('客户名称-测试' + str(timestamp), cols[0].text, '新增和查询记录的客户名称相同')
            self.assertEqual('显示名称-测试' + str(timestamp), cols[1].text, '新增和查询记录的显示名称相同')
            self.assertIn('测试部门5', cols[2].text, '新增和查询记录的所属机构相同')
            self.assertIn('管理员', cols[3].text, '新增和查询记录的所属角色相同')
            self.assertEqual('激活状态', cols[5].text, '新增和查询记录的账户状态相同')

            self.driver.find_element(By.XPATH, '//span[text()="编辑"]').click()
            time.sleep(1)
            dialog = self.driver.find_element(By.XPATH, '//div[@class="el-dialog" and @aria-label="编辑账户"]')
            dialogBody = dialog.find_element(By.XPATH, '//div[@class="el-dialog__body"]')
            formInputs = dialogBody.find_elements(By.XPATH, '//input[@class="el-input__inner"]')

            formInputs[13].clear()
            formInputs[13].send_keys('显示名称-测试编辑' + str(timestamp))

            formInputs[14].click()
            time.sleep(1)
            firstOrgTreeNode = self.driver.find_elements(By.XPATH,
                                                         '//li[contains(@class, "el-select-dropdown__item")]//span[contains(text(), "测试部门4") and @class="el-tree-node__label"]')[
                2]
            firstOrgTreeNode.click()
            formInputs[15].click()
            time.sleep(1)
            firstAccountStatusTreeNode = self.driver.find_elements(By.XPATH,
                                                                   '//li[contains(@class, "el-select-dropdown__item")]//span[text()="锁定状态"]')[
                2]
            firstAccountStatusTreeNode.click()

            self.driver.find_elements(By.XPATH, '//span[@class="el-input__suffix-inner"]')[9].click()
            time.sleep(1)

            firstRoleTreeNode = self.driver.find_elements(By.XPATH,
                                                          '//li[contains(@class, "el-select-dropdown__item")]//span[text()="hhhhhh"]')[
                2]
            firstRoleTreeNode.click()
            time.sleep(1)
            saveButton = self.driver.find_elements(By.CSS_SELECTOR,
                                                   '.el-dialog__footer:nth-child(3) .el-button--primary > span')
            saveButton[1].click()
            time.sleep(2)
            accountName.clear()
            accountFullName.clear()
            accountName.send_keys('客户名称-测试' + str(timestamp))
            accountFullName.send_keys('显示名称-测试编辑' + str(timestamp))
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            cols = el_rows[0].find_elements(By.TAG_NAME, 'span')
            self.assertEqual('客户名称-测试' + str(timestamp), cols[0].text, '编辑和查询记录的客户名称相同')
            self.assertEqual('显示名称-测试编辑' + str(timestamp), cols[1].text, '编辑和查询记录的显示名称相同')
            self.assertIn('测试部门4', cols[2].text, '编辑和查询记录的所属机构相同')
            self.assertIn('hhhhhh', cols[3].text, '编辑和查询记录的所属角色相同')
            self.assertEqual('锁定状态', cols[5].text, '编辑和查询记录的账户状态相同')

            self.driver.find_element(By.XPATH, '//span[text()="冻结"]').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//span[text()="查询"]').click()
            time.sleep(2)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            cols = el_rows[0].find_elements(By.TAG_NAME, 'span')
            self.assertEqual('注销状态', cols[5].text, '冻结功能正常')

            self.driver.find_element(By.XPATH, '//span[text()="删除"]').click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, '.el-button--default:nth-child(2) > span:nth-child(1)').click()
            time.sleep(1)
            el_rows = self.driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
            self.assertEqual(0, len(el_rows), '根据参数,删除按钮点击后查询记录为0')

        except Exception as e:
            logging.exception(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
