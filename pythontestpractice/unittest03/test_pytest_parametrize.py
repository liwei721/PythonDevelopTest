"""
    @author: xuanke
    @time: 2020/6/18
    @function: 对pytest的参数化进行验证
"""
import pytest

name_pwd_list = [("zs", "123456"), ("ls", "123456")]


# 第一种情况，直接在函数上添加参数化装饰器
@pytest.mark.parametrize(("name", "pwd"), name_pwd_list)
def test_login(name, pwd):
    print(f"{name}====={pwd}")


# 第2种情况，直接在class上添加参数化装饰器
@pytest.mark.parametrize(("name", "pwd"), name_pwd_list)
class TestCase():

    def test_login_01(self, name, pwd):
        print(f"login with name={name},pwd={pwd}")

    def test_login_02(self, name, pwd):
        print(f"login with name={name},pwd={pwd}")


# 第三种情况，在函数上有多个参数化装饰器。
data_1 = [1, 2, 3]
data_2 = ['a', 'b']


@pytest.mark.parametrize('a', data_1)
@pytest.mark.parametrize('b', data_2)
def test_many_fixture(a, b):
    pass
