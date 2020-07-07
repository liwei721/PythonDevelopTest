"""
    @author: xuanke
    @time: 2020/7/7
    @function: 对获取段子的接口进行验证
    https://api.apiopen.top/getJoke?page=1&count=2&type=video
"""
from locust import HttpUser, TaskSet, task


class UserTasks(TaskSet):

    # 列出需要测试的任务形式二
    @task(2)
    def test_joke(self):
        self.client.get("/getJoke?page=1&count=2&type=video")

    @task(1)
    def test_poetry(self):
        self.client.get("/recommendPoetry")


class WebsiteUser(HttpUser):
    host = "https://api.apiopen.top"
    min_wait = 2000
    max_wait = 5000
    tasks = [UserTasks]
