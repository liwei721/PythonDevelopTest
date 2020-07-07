"""
    @author: xuanke
    @time: 2020/7/6
    @function: 兼容使用什么单元测试框架
"""


class TestCaseRunner:

    def __init__(self, unit_type):
        self.unit_type = unit_type

        # 如果没有指定，默认使用pytest
        if self.unit_type is None or self.unit_type == '':
            self.unit_type = 'pytest'

    def exec_testcase(self, test_case_dict):
        """
        执行测试用例
        """
        test_case_dict = {}
        if

