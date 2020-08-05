"""
    @author: xuanke
    @time: 2020/7/22
    @function: 验证appium的方法。
"""
from appium import webdriver


def init_drivers():
    desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'Android Emulator',
                    'appPackage': 'tv.danmaku.bili', 'appActivity': 'tv.danmaku.bili.MainActivityV2'}
    # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


def get_info(driver):
    """
    对元素信息进行获取
    :return:
    """
    print(driver.current_activity)
    print(driver.current_package)
    print(driver.page_source)
    print(driver.contexts)

    # 判断登录页面的逻辑
    if driver.current_activity == ".ui.login.LoginActivity":
        # 执行登录操作
        # performLogin()
    else:
        # 进入首页，不执行操作。
        pass


def find_element(driver):
    """
    用于元素定位
    :return:
    """
    driver.find_element_by_id()
    driver.find_element_by_name()
    driver.find_element_by_class_name()
    driver.find_element_by_xpath()
    driver.find_element_by_link_text()
    driver.find_element_by_partial_link_text()
    driver.find_element_by_css_selector()
    driver.find_element_by_tag_name()
    # windows
    driver.find_element_by_windows_uiautomation()
    # ios相关的方法
    driver.find_element_by_ios_class_chain()
    driver.find_element_by_ios_predicate()
    driver.find_element_by_ios_uiautomation()
    # Android相关方法
    driver.find_element_by_android_data_matcher()
    driver.find_element_by_android_uiautomator()
    driver.find_element_by_android_view_matcher()
    driver.find_element_by_android_viewtag()

    # Android和ios公共的方法
    # Android是content-description，IOS是accessibility identifier
    driver.find_element_by_accessibility_id()
    driver.find_element_by_image()
    driver.find_element_by_custom()


if __name__ == '__main__':
    drivers = init_drivers()
    get_info(drivers)
