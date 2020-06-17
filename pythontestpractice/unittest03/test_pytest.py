"""
    @author: xuanke
    @time: 2020/6/17
    @function: 对pytest框架进行验证，主要对teardown进行验证
"""
import pytest


def setup_module():
    print("=====整个.py模块开始前只执行一次初始化全局资源=====")


def teardown_module():
    print("=====整个.py模块结束后只执行一次关闭全局资源=====")


def setup_function():
    print("===setup_function每个函数级别用例开始前都执行===")


def teardown_function():
    print("===teardown_function每个函数级别用例结束后都执行====")


def test_one():
    print("function one")


def test_two():
    print("function two")


class TestCase:
    def setup_class(self):
        print("====setup_class测试类开始前只执行一次====")

    def teardown_class(self):
        print("====teardown_class整个测试类结束后只执行一次====")

    def setup_method(self):
        print("==setup_method类里面每个方法用例执行前都会执行==")

    def teardown_method(self):
        print("==teardown_method类里面每个方法用例结束后都会执行==")

    def setup(self):
        print("=setup类里面每个用例执行前都会执行=")

    def teardown(self):
        print("=teardown类里面每个用例结束后都会执行==")

    def test_three(self):
        print("method three")