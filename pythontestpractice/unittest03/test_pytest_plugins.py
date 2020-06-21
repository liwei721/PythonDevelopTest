"""
    @author: xuanke
    @time: 2020/6/18
    @function: 对pytest的参数化进行验证
"""
import random
import pytest


def test_repeat_fail():
    flag = random.choice([True, False])
    print(flag)
    assert flag


@pytest.mark.repeat(5)
def test_repeat():
    print("test repeat")


def test_add():
    assert 1 + 4 == 5
    assert 1 + 3 == 3
    assert 2 + 5 == 7
    assert 2 + 6 == 8
    print("测试完成")


def test_assume_add():
    pytest.assume(1 + 4 == 5)
    pytest.assume(1 + 3 == 3)
    pytest.assume(2 + 5 == 7)
    pytest.assume(2 + 6 == 8)
    print("测试完成")


@pytest.mark.run(order=2)
def test_order1():
    print("test first")
    assert True


@pytest.mark.run(order=1)
def test_order2():
    print("test second")
    assert True


@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_rerun():
    print("test rerun")
    assert 1 == 2
