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
    desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'Android Emulator'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 获取锁屏视图
    screen_view = driver.find_element_by_id("com.android.systemui:id/lockPatternView")
    screen_size = screen_view.size
    screen_location = screen_view.location

    # 起始坐标
    start_x = screen_location.get("x")
    start_y = screen_location.get("y")
    height = screen_size.get("height")
    width = screen_size.get("width")

    # 获取每个坐标点的坐标
    el_1 = (int(start_x + width * (1 / 6) * 1), int(start_y + height * (1 / 6) * 1))
    el_2 = (int(start_x + width * (1 / 6) * 3), int(start_y + height * (1 / 6) * 1))
    el_3 = (int(start_x + width * (1 / 6) * 5), int(start_y + height * (1 / 6) * 1))
    el_4 = (int(start_x + width * (1 / 6) * 1), int(start_y + height * (1 / 6) * 3))
    el_5 = (int(start_x + width * (1 / 6) * 3), int(start_y + height * (1 / 6) * 3))
    el_6 = (int(start_x + width * (1 / 6) * 5), int(start_y + height * (1 / 6) * 3))
    el_7 = (int(start_x + width * (1 / 6) * 1), int(start_y + height * (1 / 6) * 5))
    el_8 = (int(start_x + width * (1 / 6) * 3), int(start_y + height * (1 / 6) * 5))
    el_9 = (int(start_x + width * (1 / 6) * 5), int(start_y + height * (1 / 6) * 5))

    # 点击手势，我手机上设置的是1235789
    TouchAction(driver).press(x=el_1[0], y=el_1[1]).wait(500) \
        .move_to(x=el_2[0], y=el_2[1]).wait(500) \
        .move_to(x=el_3[0], y=el_3[1]).wait(500) \
        .move_to(x=el_5[0], y=el_5[1]).wait(500) \
        .move_to(x=el_7[0], y=el_7[1]).wait(500) \
        .move_to(x=el_8[0], y=el_8[1]).wait(500) \
        .move_to(x=el_9[0], y=el_9[1]).wait(500) \
        .release().perform()


def zoom_screen():
    desired_caps = {'platformName': 'Android', 'platformVersion': '10.0', 'deviceName': 'HONOR 20s'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 首先通过屏幕的尺寸获取一个基准坐标值
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']

    # 定义两个touchAction，向相反的方向移动
    # first_action = TouchAction(driver)
    # first_action.press(x=x*0.4, y=y*0.4).wait(500).move_to(x=x*0.2, y=y*0.2).release()
    # second_action = TouchAction(driver)
    # second_action.press(x=x*0.6, y=x*0.6).wait(500).move_to(x=x*0.8, y=y*0.8).release()

    # 缩小地图
    first_action = TouchAction(driver)
    first_action.press(x=x * 0.2, y=y * 0.2).wait(500).move_to(x=x * 0.4, y=y * 0.4).release()
    second_action = TouchAction(driver)
    second_action.press(x=x * 0.8, y=x * 0.8).wait(500).move_to(x=x * 0.6, y=y * 0.6).release()

    # 定义多点触控
    multi_action = MultiAction(driver)
    multi_action.add(first_action, second_action)
    multi_action.perform()


def driver_method():
    desired_caps = {'platformName': 'Android', 'platformVersion': '10.0', 'deviceName': 'HONOR 20s'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    driver.swipe()
    driver.scroll()
    driver.drag_and_drop()
    driver.tap()
    driver.back()
    driver.forward()
    driver.flick()
    driver.shake()
    driver.unlock()
    driver.press_keycode()
    driver.lock()


def wechat_test():
    desired_caps = {'platformName': 'Android', 'platformVersion': '10.0', 'deviceName': 'HONOR 20s'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 切换到通讯录tab
    driver.tap([(270, 2189)])
    # 滑动到通讯录最底部
    driver.swipe(start_x=194, start_y=238, end_x=0, end_y=2038)
    driver.flick(start_x=0, start_y=2038, end_x=194, end_y=238)

    # 中间间隔5s钟
    time.sleep(5)

    # 切换到发现tab
    driver.tap([(540, 2189)])
    # 点击摇一摇，进入摇一摇页面
    driver.tap([(151,608)])

    time.sleep(5)
    # 模拟摇一摇
    driver.shake()


if __name__ == '__main__':
    wechat_test()
