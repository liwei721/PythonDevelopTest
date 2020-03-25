"""
    @author: xuanke
    @time: 2020/3/11
    @function: 定位元素的8中方式
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import logging
import time

logging.basicConfig(level=logging.NOTSET)


def find_element_by_id():
    """
    通过元素的id定位元素
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    try:
        start_time = time.time()
        # 通过id属性查找百度首页输入框，baidu_input_by_id是WebElement对象
        baidu_input_by_id = chrome_driver.find_element_by_id("kw")
        end_time = time.time()
        logging.debug("通过id获取元素耗时：%s", end_time - start_time)
        # 在输入框中输入 I love python
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
        start_time = time.time()
        # 通过name属性查找百度首页输入框
        baidu_input_by_name = chrome_driver.find_element_by_name("wd")
        end_time = time.time()
        logging.debug("通过name获取元素耗时：%s", end_time - start_time)
        # 输入框中输入 I love python。
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


def find_element_by_class():
    """
    通过元素的名称定位元素
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    try:
        start_time = time.time()
        # 通过name属性查找百度首页输入框
        baidu_input_by_name = chrome_driver.find_element_by_class_name("s_ipt")
        end_time = time.time()
        logging.debug("通过class获取元素耗时：%s", end_time - start_time)
        # 输入框中输入 I love python。
        baidu_input_by_name.send_keys("I love python !!")
    except NoSuchElementException as e:
        logging.debug("not found input element")
    chrome_driver.quit()


def get_baidu_img_by_tags():
    """
    通过tag获取baidu首页的图片
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    try:
        # 通过name属性查找百度首页输入框
        baidu_img_list = chrome_driver.find_elements_by_tag_name("img")
        logging.debug(len(baidu_img_list))
        for baidu_img in baidu_img_list:
            logging.debug(baidu_img.get_attribute("src"))
            if baidu_img.get_attribute("src") == 'https://www.baidu.com/img/baidu_resultlogo@2.png':
                logging.debug(baidu_img)
    except NoSuchElementException as e:
        logging.debug("not found input element")
    chrome_driver.quit()


def find_element_by_link_text():
    """
    通过链接的文本来获取元素
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    try:
        start_time = time.time()
        # 通过name属性查找百度首页输入框
        video_href = chrome_driver.find_element_by_link_text("视频")
        end_time = time.time()
        logging.debug("通过class获取元素耗时：%s", end_time - start_time)
        # 点击链接
        video_href.click()
    except NoSuchElementException as e:
        logging.debug("not found input element")
    chrome_driver.quit()


def find_element_by_xpath():
    """
    通过XPath表达式获取元素
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    try:
        start_time = time.time()
        # 通过Xpath表达式查找百度首页输入框
        baidu_input = chrome_driver.find_element_by_xpath('//*[@id="kw"]')
        end_time = time.time()
        logging.debug("通过xpath获取元素耗时：%s", end_time - start_time)
        # 输入文本
        baidu_input.send_keys("I love XPath")
    except NoSuchElementException as e:
        logging.debug("not found input element")
    chrome_driver.quit()


def find_element_by_css_selector():
    """
    通过css selector表达式获取元素
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    try:
        start_time = time.time()
        # 通过css selector表达式查找百度首页输入框
        baidu_input = chrome_driver.find_element_by_css_selector('#kw')
        end_time = time.time()
        logging.debug("通过css selector获取元素耗时：%s", end_time - start_time)
        # 输入文本
        baidu_input.send_keys("I love XPath")
    except NoSuchElementException as e:
        logging.debug("not found input element")
    chrome_driver.quit()


if __name__ == '__main__':
    find_element_by_css_selector()
