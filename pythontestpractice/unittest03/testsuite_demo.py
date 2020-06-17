"""
    @author: xuanke
    @time: 2020/6/14
    @function: 对testSuite进行验证
"""
import unittest
import sys
import importlib
import HTMLReport
from pythontestpractice.unittest03 import unittest_demo
from pythontestpractice.unittest03 import unittest_demo1


def test_suite():
    """
    对test_suite进行验证
    :return:
    """
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # 通过类加载测试用例
    suite.addTest(loader.loadTestsFromTestCase(unittest_demo.UnitTestCase))
    suite.addTest(loader.loadTestsFromTestCase(unittest_demo1.UnitTestCase1))

    # 通过模块添加测试用例
    module_demo = importlib.import_module("pythontestpractice.unittest03.unittest_demo")
    module_demo1 = importlib.import_module("pythontestpractice.unittest03.unittest_demo1")
    suite.addTest(loader.loadTestsFromModule(module_demo))
    suite.addTest(loader.loadTestsFromModule(module_demo1))

    # 通过路径添加测试用例
    suite.addTest(loader.discover(r'D:\codespace\python\PythonTestPractice\pythontestpractice\unittest03',
                                  pattern='unittest*.py'))

    # 通过名字加载测试用例
    suite.addTest(loader.loadTestsFromName('pythontestpractice.unittest03.unittest_demo.UnitTestCase.test_add'))
    suite.addTest(loader.loadTestsFromName('pythontestpractice.unittest03.unittest_demo1'))
    # 执行测试，需要用到runner，后面会介绍
    runner = unittest.TextTestRunner()
    runner.run(suite)


def test_case_run():
    """
    对testCase 和 testsuite的run方法进行验证
    :return:
    """
    # testCase的执行
    result = unittest.TextTestResult(sys.stdout, 'test result', 1)
    unittest_case = unittest_demo.UnitTestCase("test_add")
    unittest_case.run(result)

    # testsuite的执行
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(unittest_demo.UnitTestCase))
    suite.run(result)


def test_runner():
    """
    对 test的runner进行验证
    :return:
    """
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # 通过名字加载测试用例
    suite.addTest(loader.loadTestsFromName('pythontestpractice.unittest03.unittest_demo'))
    suite.addTest(loader.loadTestsFromName('pythontestpractice.unittest03.unittest_demo1'))
    # testRunner，我们将结果写到文件中
    with open("unittext.txt", "w+") as result_file:
        runner = unittest.TextTestRunner(stream=result_file, verbosity=2)
        runner.run(suite)


def test_html_report():
    """
    对HTMLReport进行验证
    :return:
    """
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # 通过名字加载测试用例
    suite.addTest(loader.loadTestsFromName('pythontestpractice.unittest03.unittest_demo'))
    suite.addTest(loader.loadTestsFromName('pythontestpractice.unittest03.unittest_demo1'))

    # 使用htmlReport
    runner = HTMLReport.TestRunner(report_file_name='test',
                                   output_path='report',
                                   title='测试报告',
                                   description='测试描述信息',
                                   sequential_execution=True)
    runner.run(suite)


if __name__ == '__main__':
    test_html_report()
