"""
    @author: xuanke
    @time: 2020/8/10
    @function: 对元素进行操作
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

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
    # 获取用户隐私协议弹窗
    agree_btn = driver.find_element_by_id("tv.danmaku.bili:id/agree")
    TouchAction(driver).tap(agree_btn).perform().release()


if __name__ == '__main__':
    tap()
