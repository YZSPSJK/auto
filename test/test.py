from login import login
from sysManage import accountManage, applicationManage, directoryManage, orgManage, roleManage, sourceManage
from tabSwitch import tabSwitch
from library.jobManage import sourceList

import unittest
from BeautifulReport import BeautifulReport


def report(file_name, test_case):
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(test_case))
    br = BeautifulReport(suite)
    br.report(filename=file_name, description='测试报告', report_dir='/Users/sjk/workspace/sjk/python/auto/testReport')


def report_all():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(login.TestCase))
    suite.addTest(loader.loadTestsFromTestCase(accountManage.TestCase))
    suite.addTest(loader.loadTestsFromTestCase(applicationManage.TestCase))
    suite.addTest(loader.loadTestsFromTestCase(directoryManage.TestCase))
    suite.addTest(loader.loadTestsFromTestCase(orgManage.TestCase))
    suite.addTest(loader.loadTestsFromTestCase(roleManage.TestCase))
    suite.addTest(loader.loadTestsFromTestCase(sourceManage.TestCase))
    suite.addTest(loader.loadTestsFromTestCase(tabSwitch.TestCase))
    br = BeautifulReport(suite)
    br.report(filename='total.html', description='测试报告', report_dir='/Users/sjk/workspace/sjk/python/auto/testReport')


if __name__ == '__main__':
    report('sourceList.html', sourceList.TestCase)
    # report('accountManage.html', accountManage.TestCase)
    # report('applicationManage.html', applicationManage.TestCase)
    # report('directoryManage.html', directoryManage.TestCase)
    # report('orgManage.html', orgManage.TestCase)
    # report('roleManage.html', roleManage.TestCase)
    # report('jobManage.html', jobManage.TestCase)
    # report('tabSwitch.html', tabSwitch.TestCase)

    # report_all()
