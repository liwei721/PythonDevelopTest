"""
    @author: xuanke
    @time: 2020/6/17
    @function: 验证pytest的mark功能
"""
import pytest


@pytest.mark.windows
def test_windows_case1():
    print("测试windows case1")


@pytest.mark.windows
def test_windows_case2():
    print("测试windows case2")


@pytest.mark.windows
def test_windows_case3():
    print("测试windows case3")


@pytest.mark.mac
def test_mac_case1():
    print("测试mac case1")


@pytest.mark.mac
def test_mac_case2():
    print("测试mac case2")


@pytest.mark.mac
class TestClass:
    def test_method(self):
        print("测试 class mac")


def test_noMark():
    print("没有标记测试")
