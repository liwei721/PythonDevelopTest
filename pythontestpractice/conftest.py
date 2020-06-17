"""
    @author: xuanke
    @time: 2020/6/17
    @function: 全局的conftest.py配置文件
"""
import pytest


@pytest.fixture
def init():
    print("init webdriver")
