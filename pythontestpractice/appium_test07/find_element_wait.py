"""
    @author: xuanke
    @time: 2020/8/23
    @function: 通过Image来定位元素。
"""
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_force():
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '10.0',
                    'deviceName': 'HONOR 20S',
                    'appPackage': 'com.ss.android.ugc.aweme',
                    'appActivity': 'com.ss.android.ugc.aweme.main.MainActivity'}
    # 连接appium server
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 为了弹窗出现。强制等待 5s再进行操作。
    time.sleep(5)
    # 获取用户隐私协议弹窗
    agree_btn = driver.find_element_by_id("com.ss.android.ugc.aweme:id/ahw")
    agree_btn.click()
    # 为了弹窗出现。强制等待 5s再进行操作。
    time.sleep(5)
    # 获取位置权限授权的弹框,仅在使用时允许
    get_device_info = driver.find_element_by_id(
        "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    get_device_info.click()
    # 为了弹窗出现。强制等待 5s再进行操作。
    time.sleep(5)
    # 获取设备信息的弹框
    always_allow = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
    always_allow.click()
    # 强制等待 10s再进行操作。
    time.sleep(10)
    # 上滑屏幕
    driver.swipe(start_x=200, start_y=500, end_x=200, end_y=0)


def wait_implicitly():
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '10.0',
                    'deviceName': 'HONOR 20S',
                    'appPackage': 'com.ss.android.ugc.aweme',
                    'appActivity': 'com.ss.android.ugc.aweme.main.MainActivity'}
    # 连接appium server
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 为了弹窗出现。强制等待 5s再进行操作。
    driver.implicitly_wait(5)
    # 获取用户隐私协议弹窗
    agree_btn = driver.find_element_by_id("com.ss.android.ugc.aweme:id/ahw")
    agree_btn.click()
    # 获取位置权限授权的弹框,仅在使用时允许
    get_device_info = driver.find_element_by_id(
        "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    get_device_info.click()
    # 获取设备信息的弹框
    always_allow = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
    always_allow.click()
    # 上滑屏幕
    driver.swipe(start_x=200, start_y=500, end_x=200, end_y=0)


def wait_explicit():
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '10.0',
                    'deviceName': 'HONOR 20S',
                    'appPackage': 'com.ss.android.ugc.aweme',
                    'appActivity': 'com.ss.android.ugc.aweme.main.MainActivity'}
    # 连接appium server
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 为了弹窗出现。强制等待 5s再进行操作。
    wait_element = WebDriverWait(driver, 5)
    # 获取用户隐私协议弹窗
    agree_btn = wait_element.until(EC.visibility_of_element_located((By.ID, "com.ss.android.ugc.aweme:id/ahw")))
    agree_btn.click()
    # 获取位置权限授权的弹框,仅在使用时允许
    get_device_info = wait_element.until(EC.visibility_of_element_located((By.ID,
                                                                           "com.android.permissioncontroller:id"
                                                                           "/permission_allow_foreground_only_button")))
    get_device_info.click()
    # 获取设备信息的弹框
    always_allow = wait_element.until(
        EC.visibility_of_element_located((By.ID, "com.android.permissioncontroller:id/permission_allow_button")))
    always_allow.click()
    # 上滑屏幕
    driver.swipe(start_x=200, start_y=500, end_x=200, end_y=0)


if __name__ == '__main__':
    wait_explicit()
