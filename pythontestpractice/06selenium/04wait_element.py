"""
    @author: xuanke
    @time: 2020/3/21
    @function: 实现元素等待
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import time
import logging

from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s')


def test_thread_wait():
    """
     验证线程等待
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    try:
        # 通过id属性查找百度首页输入框，baidu_input_by_id是WebElement对象
        baidu_input_by_id = chrome_driver.find_element_by_id("kw")
        time.sleep(5)
        # 在输入框中输入 I love python
        baidu_input_by_id.send_keys("I love python !!")
        time.sleep(5)
    except NoSuchElementException as e:
        logging.debug("not found input element")
    chrome_driver.quit()


def test_implicitly_wait():
    """
    验证隐式等待
    :return:
    """
    chrome_driver = webdriver.Chrome()
    # 设置等待10s时间
    chrome_driver.implicitly_wait(10)
    chrome_driver.get("https://github.com/")
    try:
        # 通过css selector查找元素
        first_element = chrome_driver.find_element_by_name('q')
        first_element.send_keys("myProject")
        logging.debug("locate the second element")
        # 故意写错id，让它找不到元素
        second_element = chrome_driver.find_element_by_name('userqq')
    except NoSuchElementException as e:
        logging.debug("not found input element")

    chrome_driver.quit()


def test_display_wait():
    """
    验证显示等待
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    webdriver_wait = WebDriverWait(chrome_driver, 5)
    try:
        # 通过id属性查找百度首页输入框，baidu_input_by_id是WebElement对象
        baidu_input_by_id = webdriver_wait.until(EC.visibility_of_element_located((By.ID, "kw")))
        logging.info(baidu_input_by_id)
        # # 在输入框中输入 I love python
        baidu_input_by_id.send_keys("I love python !!")
        time.sleep(5)
    except NoSuchElementException as e:
        logging.debug("not found input element")
    chrome_driver.quit()


def test_display_wait_alert():
    """
    验证显示等待中的弹框
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    webdriver_wait = WebDriverWait(chrome_driver, 5)
    try:
        # 这里肯定是没有弹窗的，只是模拟方法调用
        baidu_alert = webdriver_wait.until(EC.alert_is_present())
        if baidu_alert:
            logging.debug(baidu_alert.text)
            baidu_alert.accept()
        else:
            logging.debug('no alert')
    except NoSuchElementException as e:
        logging.debug("not found input element")
    chrome_driver.quit()


def test_display_wait_element_visible():
    """
    验证显示等待中元素是否可见
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    webdriver_wait = WebDriverWait(chrome_driver, 5)
    try:
        # 获取百度首页输入框
        baidu_input = webdriver_wait.until(EC.visibility_of_element_located((By.ID, "kw")))
        baidu_input.send_keys("Hello python")
    except NoSuchElementException as e:
        logging.debug("not found input element")
    chrome_driver.quit()


def test_display_wait_element_present():
    """
    验证显示等待中是否存在元素
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    webdriver_wait = WebDriverWait(chrome_driver, 5)
    try:
        # 获取百度首页输入框
        baidu_presence_element = webdriver_wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#form > input[type=hidden]:nth-child(6)")))
    except NoSuchElementException as e:
        logging.debug("not found input element")
    chrome_driver.quit()


def test_display_wait_element_clickable():
    """
    验证显示等待中元素是否可以点击
    :return:
    """
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.baidu.com")
    webdriver_wait = WebDriverWait(chrome_driver, 5)
    try:
        # 获取百度首页按钮
        baidu_btn = webdriver_wait.until(EC.element_to_be_clickable((By.ID, "su")))
        baidu_btn.click()
    except NoSuchElementException as e:
        logging.debug("not found input element")
    chrome_driver.quit()


if __name__ == '__main__':
    test_display_wait_element_present()
