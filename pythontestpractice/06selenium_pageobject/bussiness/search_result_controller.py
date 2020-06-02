"""
    @author: xuanke
    @time: 2020/3/28
    @function: 搜索结果页的业务逻辑
"""
from page.search_result_page import SearchResultPage


class SearchResultController():

    def __init__(self, driver):
        self.driver = driver
        self.searchResultPage = SearchResultPage(driver)

    def get_error_tips(self):
        """
        获取错误提示文案
        :return:
        """
        return self.searchResultPage.get_error_tips().strip()
