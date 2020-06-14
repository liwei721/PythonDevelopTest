"""
    @author: xuanke
    @time: 2020/6/14
    @function: 验证多个测试用例
"""
import unittest
from pythontestpractice.unittest03 import modueA


class UnitTestCase1(unittest.TestCase):

    def setUp(self) -> None:
        print("UnitTestCase1 setup")

    def tearDown(self) -> None:
        print("UnitTestCase1 tearDown")

    @classmethod
    def setUpClass(cls) -> None:
        print("UnitTestCase1 setUpclass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("UnitTestCase1 tearDownClass")

    def test_add(self):
        print("UnitTestCase1 test_add")
        self.assertEqual(modueA.add(1, 2), 3)

    def test_div(self):
        print("UnitTestCase1 test_div")
        self.assertEqual(modueA.div(2, 3), 6)
