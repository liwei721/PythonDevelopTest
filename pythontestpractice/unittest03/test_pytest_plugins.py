"""
    @author: xuanke
    @time: 2020/6/18
    @function: 对pytest的参数化进行验证
"""
import random


def test_repeat_fail():
    flag = random.choice([True, False])
    print(flag)
    assert flag
