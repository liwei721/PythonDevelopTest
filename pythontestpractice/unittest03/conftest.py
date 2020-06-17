"""
    @author: xuanke
    @time: 2020/6/17
    @function: 子模块中的conftest
"""
import pytest


@pytest.fixture()
def login():
    print("login  first")
