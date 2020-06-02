"""
    @author: xuanke
    @time: 2020/3/26
    @function: 首页逻辑处理层
"""
from page.home_page import HomePage


class HomeController(object):

    def __init__(self, driver):
        self.driver = driver

    def search_keyword(self, word):
        """
        B站首页输入框搜索内容
        :param word:
        :return:
        """
        # 输入内容
        home_page = HomePage(self.driver)
        home_page.input_search_word(word)

        # 点击Enter按键
        home_page.press_enter_key()

        # 切换window handle
        home_page.switch_to_current_window()

    def close_window(self):
        """
        关闭窗口
        :return:
        """
        self.driver.quit()
