"""
    @author: xuanke
    @time: 2020/3/28
    @function: 测试用例的基类,在基类中可以封装对WebDriver的统一处理逻辑
"""
from selenium import webdriver


class TestBase(object):

    @classmethod
    def get_driver(cls):
        driver = webdriver.Chrome()
        driver.get("https://www.bilibili.com/")
        return driver