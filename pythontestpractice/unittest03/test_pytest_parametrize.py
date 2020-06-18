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
class TestCase:

    def test_login_01(self, name, pwd):
        print(f"login with name={name},pwd={pwd}")

    def test_login_02(self, name, pwd):
        print(f"login with name={name},pwd={pwd}")


# 第3中情况通过ids修改用例名称
ids = ["{} login system use pwd {}".format(name, pwd) for name, pwd in name_pwd_list]


@pytest.mark.parametrize(("name", "pwd"), name_pwd_list, ids=ids)
def test_ids(name, pwd):
    print("name is {}, pwd is {}".format(name, pwd))


# # 第4种情况，在函数上有多个参数化装饰器。
do_list = ["swim", "play", "eat"]
name_list = ['zhangsan', 'lisi']


@pytest.mark.parametrize('do', do_list)
@pytest.mark.parametrize('name', name_list)
def test_many_fixture(name, do):
    print(f"{name} has do {do}")


# 第5种情况，indirect=True
user_data = [('lisi', '23'), ('zhangsan', '25'), ('wangwu', '27')]


@pytest.fixture()
def user_info(request):
    param = request.param
    print("{} is {} year old".format(param[0], param[1]))
    return param


@pytest.mark.parametrize("user_info", user_data, indirect=True)
def test_get_user_info(user_info):
    print("I'm {}, {} years old".format(user_info[0], user_info[1]))
