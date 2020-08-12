"""
    @author: xuanke
    @time: 2020/8/10
    @function: 对元素进行操作
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

import time

"""
 点击  element.click()
 文本框输入内容  element.sendkeys()
 手指触摸屏幕    tap
 短按   press（）
 长按   long_press
 模拟双击   double_click
 移动手指  move_to
 多点触控  multiAction
 等待一段时间操作   wait
"""


def tap():
    desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'Android Emulator',
                    'appPackage': 'tv.danmaku.bili', 'appActivity': 'tv.danmaku.bili.MainActivityV2'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 获取用户隐私协议弹窗,点击同意。
    agree_btn = driver.find_element_by_id("tv.danmaku.bili:id/agree")
    TouchAction(driver).tap(agree_btn).perform().release()

    # 需要初始化数据，所以暂停15s
    time.sleep(15)
    # 进入首页，点击左上角登录按钮
    # 通过x,y坐标执行tap bounds=[50,116][182,248]
    TouchAction(driver).tap(x=141, y=240).perform().release()


def press():
    desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'Android Emulator',
                    'appPackage': 'tv.danmaku.bili', 'appActivity': 'tv.danmaku.bili.MainActivityV2'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 点击同意用户协议
    agree_btn = driver.find_element_by_id("tv.danmaku.bili:id/agree")
    TouchAction(driver).press(agree_btn).perform().release()


def long_press():
    desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'Android Emulator',
                    'appPackage': 'tv.danmaku.bili', 'appActivity': 'tv.danmaku.bili.MainActivityV2'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 点击同意用户协议
    agree_btn = driver.find_element_by_id("tv.danmaku.bili:id/agree")
    agree_btn.click()

    # 中间暂停15s
    time.sleep(15)

    # 长按视频，弹出添加反馈
    TouchAction(driver).long_press(x=353, y=1200, duration=5000).perform().release()


def long_press_impl():
    desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'Android Emulator',
                    'appPackage': 'tv.danmaku.bili', 'appActivity': 'tv.danmaku.bili.MainActivityV2'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 点击同意用户协议
    agree_btn = driver.find_element_by_id("tv.danmaku.bili:id/agree")
    agree_btn.click()

    # 中间暂停15s
    time.sleep(30)
    # 长按视频，弹出添加反馈
    # video = driver.find_element_by_id("tv.danmaku.bili:id/cover")
    TouchAction(driver).press(x=353, y=1200).wait(10000).perform().release()


def move_to():
    desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'Android Emulator',
                    'appPackage': 'tv.danmaku.bili', 'appActivity': 'tv.danmaku.bili.MainActivityV2'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 点击同意用户协议
    agree_btn = driver.find_element_by_id("tv.danmaku.bili:id/agree")
    agree_btn.click()
    TouchAction(driver).press(x=233, y=344).move_to(x=234, y=345).perform().release()


if __name__ == '__main__':
    long_press_impl()
