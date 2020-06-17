"""
    @author: xuanke
    @time: 2020/6/17
    @function: 验证fixture的conftest.py模块
"""
import pytest


@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("init")
def test_conftest():
    print("test conftest")
