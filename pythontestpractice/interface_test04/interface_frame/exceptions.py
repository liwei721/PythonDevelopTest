"""
    @author: xuanke
    @time: 2020/7/6
    @function: 自定义一个异常类，封装各类异常
"""


class MyBaseFailure(Exception):
    pass


class TestCasePathFailure(MyBaseFailure):
    pass


class NotSupportFormatFailure(MyBaseFailure):
    pass
