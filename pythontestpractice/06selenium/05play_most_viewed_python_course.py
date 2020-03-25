"""
    @author: xuanke
    @time: 2020/3/23
    @function: 在B站搜索python视频，并且找到播放量最高的视频，点击播放。
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC
import time


def play_top_video():
    """
      点击播放B站上播放量最高的视频
    """
    chrome_driver = webdriver.Chrome()
    # 访问b站
    chrome_driver.get("https://www.bilibili.com/")

    # 显示等待5s
    chrome_driver_wait = WebDriverWait(chrome_driver, 5)
    try:
        # 0.0 找到对应的搜索输入框
        search_input = chrome_driver_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "nav-search-keyword")))
        # 0.1 在搜索框输入python
        search_input.send_keys("python")
        # 两种方式，一种是按Enter，一种是找到搜索按钮。
        # 1. 按Enter键
        ActionChains(chrome_driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

        # 2. 找到搜索按钮
        # search_btn = chrome_driver.find_element_by_class_name("nav-search-btn")
        # search_btn.click()

        # 3.0 因为点击搜索之后，新打开了一个页面，所以需要切换窗口句柄到新打开的页面。
        window_handles = chrome_driver.window_handles
        print(window_handles)
        print(window_handles[0])
        chrome_driver.switch_to.window(window_handles[len(window_handles) - 1])

        # 3.1 按照点击量排序，找到“最多点击”，并且点击它
        top_click = chrome_driver_wait.until(EC.visibility_of_element_located(
            (By.LINK_TEXT, "最多点击")))
        top_click.click()

        # 4. 找到第一个视频并且点击，跳转到视频详情页
        first_video = chrome_driver_wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@class="video-list clearfix"]/li[1]/div/div[1]/a')))
        first_video.click()

        # 5.0 切换到新的tab页面，因为进入到了视频详情页。
        window_handles = chrome_driver.window_handles
        print(window_handles)
        print(window_handles[0])
        chrome_driver.switch_to.window(window_handles[len(window_handles) - 1])

        # 5.1 在播放页面找到播放按钮
        play_btn = chrome_driver_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bilibili-player-video-state")))
        chrome_driver.execute_script("arguments[0].click();", play_btn)

        # 6. 为了播放效果，延迟10s钟关闭。
        time.sleep(10)
    except NoSuchElementException as no_element_exec:
        print(no_element_exec)
        chrome_driver.quit()


if __name__ == '__main__':
    play_top_video()
