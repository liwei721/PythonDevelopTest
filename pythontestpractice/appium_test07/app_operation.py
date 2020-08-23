"""
    @author: xuanke
    @time: 2020/8/19
    @function: 对app的操作
"""
from appium import webdriver
import time


def all_method():
    desired_caps = {'platformName': 'Android', 'platformVersion': '10.0', 'deviceName': 'HONOR 20s'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    driver.lock()
    driver.unlock()
    driver.is_locked()
    driver.save_screenshot()
    driver.toggle_wifi()
    driver.toggle_touch_id_enrollment()
    driver.toggle_location_services()
    driver.install_app()
    driver.remove_app()
    driver.is_app_installed()
    driver.close_app()
    driver.launch_app()
    driver.background_app()
    driver.reset()
    driver.wait_activity()
    driver.touch_id()
    driver.terminate_app()
    driver.back()
    driver.forward()


def lock_and_unlock():
    desired_caps = {'platformName': 'Android', 'platformVersion': '10.0', 'deviceName': 'HONOR 20s'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 先判断是否被锁定
    if driver.is_locked():
        print('is lock')
        driver.unlock()
        # 执行解锁密码操作
    else:
        print('no lock')
        driver.lock()


def save_img():
    desired_caps = {'platformName': 'Android', 'platformVersion': '10.0', 'deviceName': 'HONOR 20s'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # 保存截图
    driver.save_screenshot("test.png")


def install_and_uninstall_app():
    desired_caps = {'platformName': 'Android', 'platformVersion': '10.0', 'deviceName': 'HONOR 20s'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 先判断是否已经安装百度地图
    if driver.is_app_installed("com.baidu.BaiduMap"):
        print('app is installed')
        # 已经安装则卸载重装
        driver.remove_app("com.baidu.BaiduMap")
        driver.install_app('D:\\com.baidu.BaiduMap_15.0.0_1000.apk')
    else:
        print('app is not installed')
        # 如果没有安装，则直接安装
        driver.install_app('D:\\com.baidu.BaiduMap_15.0.0_1000.apk')


def close_launch_app():
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '10.0',
                    'deviceName': 'HONOR 20s',
                    'appPackage': 'tv.danmaku.bili',
                    'appActivity': 'tv.danmaku.bili.ui.splash.SplashActivity'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 先关掉app
    driver.close_app()
    # 再打开app
    driver.launch_app()

    # 先将app至于后台,10s后
    driver.background_app(10)


def browser_back_forward():
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '10.0',
                    'deviceName': 'HONOR 20s',
                    'appPackage': 'com.huawei.browser',
                    'appActivity': 'com.huawei.browser.LauncherWithWindowStart'}
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.get("http://www.baidu.com")
    time.sleep(5)
    # 后退
    driver.back()
    # 前进
    driver.forward()
    # 刷新
    driver.refresh()


if __name__ == '__main__':
    browser_back_forward()
