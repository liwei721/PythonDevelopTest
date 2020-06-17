"""
    @author: xuanke
    @time: 2020/6/16
    @function: 对pytest fixture进行验证
"""
import pytest


@pytest.fixture()
def login():
    print("login first")


@pytest.fixture()
def execute():
    print("execute something")


# 第一种调用方式，作为参数传入
def test_case1(login):
    print("need login first")


def test_case2():
    print("no need login first")


# 第二种调用方式，使用装饰器
@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("execute")
def test_case3():
    print("need login first")


@pytest.mark.usefixtures("login")
def case4():
    print("test case4")


@pytest.mark.usefixtures("login")
class TestCase:

    # 第三种调用方式，使用autouse=True
    @pytest.fixture(scope="class", autouse=True)
    def get_info(self):
        print("auto get info")

    def test_get_info(self):
        print("test get info")

    def test_login(self):
        print("test login first")
