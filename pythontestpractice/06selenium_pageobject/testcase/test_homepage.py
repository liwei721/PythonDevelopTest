"""
    @author: xuanke
    @time: 2020/3/26
    @function: B站首页的testcase
"""
from .base import TestBase
from bussiness.home_controller import HomeController
from bussiness.search_result_controller import SearchResultController
import pytest


class TestHomepage(TestBase):

    @classmethod
    def setup_class(cls):
        cls.driver = cls.get_driver()
        cls.home_controller = HomeController(cls.driver)
        cls.search_result_controller = SearchResultController(cls.driver)

    def test_search_blank(self):
        """
        搜索空白字符串
        :return:
        """
        self.home_controller.search_keyword("   ")
        assert "查询参数错误" == self.search_result_controller.get_error_tips()
        self.home_controller.close_window()
