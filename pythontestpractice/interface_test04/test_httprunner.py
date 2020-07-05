"""
    @author: xuanke
    @time: 2020/7/5
    @function: 对HttpRunner的功能进行验证，以获取段子的接口为例
"""
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestJoke(HttpRunner):
    config = (
        Config("test joke interface")
            .variables(
            **{
                "num": 2,
                "type": "video"
            }
        )
            .base_url("https://api.apiopen.top")
            .verify(False)  # 不进行TLS证书校验
            .export(*["sid"])  # 导出变量sid，是每个段子的id
    )

    teststeps = [
        Step(
            RunRequest("获取内涵段子")
                .with_variables(
                **{
                    "page": 1
                }
            )
                .get("/getJoke")
                .with_params(**{"page": "$page", "count": "$num", "type": "$type"})
                .with_headers(**{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                               "like Gecko) Chrome/80.0.3987.132 Safari/537.36"})
                .extract()
                .with_jmespath("body.result[1].sid", "sid")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 200)
                .assert_length_equal("body.result[*]", 2)
        )
    ]


if __name__ == '__main__':
    TestJoke().test_start()
