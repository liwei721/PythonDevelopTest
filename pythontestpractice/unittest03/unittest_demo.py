"""
    @author: xuanke
    @time: 2020/6/14
    @function: 对unittest进行验证
"""
import unittest
import sys

from pythontestpractice.unittest03 import modueA


class UnitTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("tearDown")

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpclass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_add(self):
        print("test_add")
        self.assertEqual(modueA.add(1, 2), 3)

    def test_div(self):
        print("test_div")
        self.assertEqual(modueA.div(2, 3), 6)

    @unittest.skip("暂时不执行")
    def test_div_2(self):
        print("test_div")
        self.assertEqual(modueA.div(2, 0), 0)

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_add_2(self):
        print("test_add")
        self.assertEqual(modueA.add(1, 2), 3)

    @unittest.expectedFailure
    def test_div_3(self):
        print("test_div")
        self.assertEqual(modueA.div(2, 3), 8)
