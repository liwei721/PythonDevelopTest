"""
    @author: xuanke
    @time: 2020/6/21
    @function: 对单元测试覆盖率进行验证
"""
from pythontestpractice.unittest03.cov_demo import function


def test_add():
    assert function.add(1, 2) == 3
    assert function.add(1, 5) == 3


def test_div():
    assert function.multi(1, 2) == 3
    assert function.multi(1, 5) == 5
