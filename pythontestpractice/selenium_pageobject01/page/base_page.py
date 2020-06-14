"""
    @author: xuanke
    @time: 2020/3/26
    @function: 页面基类，封装对页面的基本操作。
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """
        打开链接
        :param url:
        :return:
        """
        self.driver.get(url)

    def find_element(self, *loc):
        """
        查找元素
        :param loc: *loc表示会将传入的tuple解析成对应的参数
        :return:
        """
        return self.driver.find_element(*loc)

    def find_element_show_wait(self, loc, time_wait):
        """
        查找元素，并且显示等待
        :param time_wait: 需要显示等待的时长
        :param loc: *loc表示会将传入的tuple解析成对应的参数
        :return:
        """
        webdriver_wait = WebDriverWait(self.driver, time_wait)
        print(loc)
        return webdriver_wait.until(EC.visibility_of_element_located(loc))

    def press_enter_key(self):
        """
        按键盘上的Enter按键
        :param key:
        :return:
        """
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    def switch_to_current_window(self):
        """
        切换当前的窗口句柄为最新的窗口（最近一次跳转的窗口）
        :return:
        """
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[len(window_handles) - 1])

    def close_window(self):
        self.driver.close()

    def quit_window(self):
        self.driver.quit()