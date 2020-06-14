"""
    @author: xuanke
    @time: 2020/3/26
    @function: 搜索结果页
"""
from .base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResultPage(BasePage):

    error_panel_by = (By.XPATH, '//*[@class="flow-loader-state"]/div/div/p')

    def __init__(self, driver):
        super().__init__(driver)

    def get_error_tips(self):
        """
        获取错误提示内容
        :return:
        """
        error_element = self.find_element_show_wait(SearchResultPage.error_panel_by, 5)
        error_tips = error_element.get_attribute('textContent')
        return error_tips


