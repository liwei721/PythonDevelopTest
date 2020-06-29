"""
    @author: xuanke
    @time: 2020/6/30
    @function: 使用pytest+requests对某个接口进行测试
"""
import requests


def test_get_joke_info():
    url = "https://api.apiopen.top/getJoke?page=1&count=2&type=video"
    header = {"Content-Type": "application/json;charset=UTF-8",
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/80.0.3987.132 Safari/537.36"}
    resp = requests.get(url, headers=header)
    status_code = resp.status_code
    resp_body = resp.json()
    print(status_code)
    print(resp_body)
