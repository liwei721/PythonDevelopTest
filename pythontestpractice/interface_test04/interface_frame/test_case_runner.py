"""
    @author: xuanke
    @time: 2020/7/6
    @function: 兼容使用什么单元测试框架
"""


class TestCaseHandler(object):

    def __init__(self, test_case_path):
        self.test_case_path = test_case_path

    def parse(self):
        """
        对测试用例进行解析
        """
