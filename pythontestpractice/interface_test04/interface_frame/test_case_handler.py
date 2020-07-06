"""
    @author: xuanke
    @time: 2020/7/6
    @function: 对测试用例进行处理
"""
import os

from pythontestpractice.interface_test04.interface_frame.exceptions import TestCasePathFailure, NotSupportFormatFailure


class TestCaseHandler(object):

    def __init__(self, test_case_path):
        self.test_case_path = test_case_path

    def parse(self):
        """
        对测试用例进行解析
        """
        if self.test_case_path is None or self.test_case_path == '':
            raise TestCasePathFailure("测试用例路径为空")

        # 判断是目录，还是文件
        if os.path.isfile(self.test_case_path):
            # 是文件则解析
            pass
        else:
            # 是目录，对目录进行遍历获取文件
            pass

    def __parse_file(self):
        """
        对测试用例配置文件真正解析的地方
        :return:
        """
        if self.test_case_path.endswith(".yml"):
            # 对yaml文件进行处理
            pass
        elif self.test_case_path.endswith(".json"):
            # 对json文件进行处理
            pass
        elif self.test_case_path.endswith(".har"):
            # 对har文件进行处理
            pass
        elif self.test_case_path.endswith(".xls"):
            # 对excel文件进行处理
            pass
        else:
            # 抛出异常，不支持的测试用例格式。
            raise NotSupportFormatFailure("不支持的测试用例格式")

    def __parse_yaml_file(self):
        """
        解析yaml文件
        :return:
        """