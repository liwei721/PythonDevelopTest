"""
    @author: xuanke
    @time: 2020/6/14
    @function: 对testSuite进行验证
"""
import unittest
import os
import types

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
    m = types.ModuleType("m")
    suite.addTest(loader.loadTestsFromModule(m))
    suite.addTest(loader.loadTestsFromModule(m))

    # 通过路径添加测试用例
    suite.addTest(loader.discover(r'D:\codespace\python\PythonTestPractice\pythontestpractice\unittest03', pattern='unittest*.py'))

    # 通过名字加载测试用例
    suite.addTest(loader.loadTestsFromName('pythontestpractice.unittest03.unittest_demo'))
    suite.addTest(loader.loadTestsFromName('pythontestpractice.unittest03.unittest_demo1'))
    # 执行测试，需要用到runner，后面会介绍
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    test_suite()
