"""
    @author: xuanke
    @time: 2020/6/21
    @function: 对pytest的分布式进行验证
"""
import time


def test_first():
    time.sleep(5)
    assert 3 == 3


def test_second():
    time.sleep(5)
    assert 3 == 3


def test_third():
    time.sleep(5)
    assert 3 == 3


def test_forth():
    time.sleep(5)
    assert 3 == 3


def test_fifth():
    time.sleep(5)
    assert 3 == 3
