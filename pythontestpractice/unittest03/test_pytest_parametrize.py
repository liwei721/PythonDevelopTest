"""
    @author: xuanke
    @time: 2020/6/18
    @function: 对pytest的参数化进行验证
"""
import pytest


@pytest.mark.parametrize(("name", "pwd"), [("zs", "123456"), ("ls", "123456")])
def test_login(name, pwd):
    print(f"{name}====={pwd}")
