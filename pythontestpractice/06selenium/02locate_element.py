"""
    @author: xuanke
    @time: 2020/3/11
    @function: 定位元素的8中方式
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import logging

logging.basicConfig(level=logging.NOTSET)


def find_element_by_id():
    """
    通过元素的id定位元素
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    try:
        # 通过id属性查找百度首页输入框，baidu_input_by_id是WebElement对象
        baidu_input_by_id = chrome_driver.find_element_by_id("kw")
        baidu_input_by_id.send_keys("I love python !!")
    except NoSuchElementException as e:
        logging.debug("not found input element")
    chrome_driver.quit()


def find_element_by_name():
    """
    通过元素的名称定位元素
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    try:
        # 通过name属性查找百度首页输入框
        baidu_input_by_name = chrome_driver.find_element_by_name("wd")
        baidu_input_by_name.send_keys("I love python !!")
    except NoSuchElementException as e:
        logging.debug("not found input element")
    chrome_driver.quit()


def find_element_by_tag_name():
    """
    通过tagName查找元素，返回匹配到的第一个元素
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    # 通过img标签过滤百度首页的图片
    try:
        baidu_images_by_tag = chrome_driver.find_element_by_tag_name("img")
        # 打印图片的链接
        logging.debug(baidu_images_by_tag.get_attribute("src"))
    except NoSuchElementException as e:
        logging.debug("not found img element")
    chrome_driver.quit()


if __name__ == '__main__':
    find_element_by_name()
