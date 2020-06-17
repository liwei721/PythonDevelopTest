"""
    @author: xuanke
    @time: 2020/6/17
    @function: 验证pytest中的skip
"""
import pytest
import sys


@pytest.fixture(autouse=True)
def login():
    print("====login====")


def test_case01():
    print("case 01")


@pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
def test_case02():
    print("case 02")


@pytest.mark.skipif(sys.platform == "win32", reason="不执行该用例！！因为没写好！！")
def test_case03():
    print("case 03")


def test_case04():
    n = 1
    while True:
        print(f"这是我第{n}条用例")
        n += 1
        if n == 5:
            pytest.skip("我跑五次了不跑了")


class Test1:

    def test_1(self):
        print("class testcase 1")

    @pytest.mark.skip(reason="不想执行")
    def test_2(self):
        print("class testcae 2")


@pytest.mark.skip(reason="直接跳过类")
class TestSkip:
    def test_1(self):
        print("class skip，so case also skip")
