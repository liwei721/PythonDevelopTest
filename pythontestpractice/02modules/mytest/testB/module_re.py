"""
    @author: xuanke
    @time: 2020/5/28
    @function: 对正则表达式验证
"""
import re


def test_match_b():
    """
    对\b进行验证
    :return:
    """
    result = re.split('\\b', '(我是传奇   传奇人生)你信吗？')
    print(result)
    result = re.split('\\B', '(我是传奇   传奇人生)你信吗？')
    print(result)


if __name__ == '__main__':
    test_match_b()
