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


def find_element_by_name():
    desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'Android Emulator',
                    'appPackage': 'tv.danmaku.bili', 'appActivity': 'tv.danmaku.bili.MainActivityV2'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 添加时间间隔,暂时先使用time.sleep线程中断
    time.sleep(15)

    # 登录按钮
    btn_login = driver.find_element_by_name("登录")
    btn_login.click()


def find_element_by_android_uiautomator():
    desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'Android Emulator',
                    'appPackage': 'tv.danmaku.bili', 'appActivity': 'tv.danmaku.bili.MainActivityV2'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 获取用户隐私协议弹窗
    agree_btn = driver.find_element_by_id("tv.danmaku.bili:id/agree")
    agree_btn.click()
    # 添加时间间隔,暂时先使用time.sleep线程中断
    time.sleep(20)
    btn_login = driver.find_element_by_android_uiautomator("new UiSelector().text(\"登录\")")
    btn_login.click()


def find_element_by_class_name():
    desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'Android Emulator',
                    'appPackage': 'tv.danmaku.bili', 'appActivity': 'tv.danmaku.bili.MainActivityV2'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 获取用户隐私协议弹窗
    agree_btn = driver.find_element_by_id("tv.danmaku.bili:id/agree")
    agree_btn.click()
    # 添加时间间隔,暂时先使用time.sleep线程中断
    time.sleep(15)
    # 获取界面中的所有的ImageView
    elements = driver.find_elements_by_class_name("android.widget.ImageView")
    # 打印程序的上下文
    print(driver.contexts)
    # 点击界面上第一个ImageView。
    elements[0].click()


def find_element_by_xpath():
    desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'Android Emulator',
                    'appPackage': 'tv.danmaku.bili', 'appActivity': 'tv.danmaku.bili.MainActivityV2'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 获取用户隐私协议弹窗
    agree_btn = driver.find_element_by_id("tv.danmaku.bili:id/agree")
    agree_btn.click()
    # 添加时间间隔,暂时先使用time.sleep线程中断
    time.sleep(15)

    login_btn = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view"
        ".ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget"
        ".FrameLayout/android.widget.FrameLayout/android.widget.ImageView")
    login_btn.click()


if __name__ == '__main__':
    find_element_by_xpath()
