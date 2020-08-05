"""
    @author: xuanke
    @time: 2020/8/5
    @function: 对界面元素的定位方法验证
"""
from appium import webdriver
import time


def find_element_by_id():
    desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'Android Emulator',
                    'appPackage': 'tv.danmaku.bili', 'appActivity': 'tv.danmaku.bili.MainActivityV2'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 获取用户隐私协议弹窗
    agree_btn = driver.find_element_by_id("tv.danmaku.bili:id/agree")
    agree_btn.click()
    # 添加时间间隔,暂时先使用time.sleep线程中断
    time.sleep(15)
    # 获取登录按钮
    btn_login = driver.find_element_by_id("tv.danmaku.bili:id/avatar")
    btn_login.click()


if __name__ == '__main__':
    find_element_by_id()
