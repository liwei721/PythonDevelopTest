"""
    @author: xuanke
    @time: 2020/3/26
    @function: 首页元素
"""
from selenium.webdriver.common.by import By

from .base_page import BasePage


class HomePage(BasePage):
    # 输入框
    search_input = (By.CLASS_NAME, 'nav-search-keyword')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def input_search_word(self, word):
        """
        输入框输入关键字
        :param word:
        :return:
        """
        search_input_element = self.find_element_show_wait(HomePage.search_input, 5)
        search_input_element.send_keys(word)