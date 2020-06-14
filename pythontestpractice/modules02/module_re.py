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


def test_find_match():
    """
    对正则表达式查找和匹配的进行验证
    :return:
    """
    # 能匹配到
    result = re.match("abc", "abcaaaa")
    print(result.group())
    print(type(result))
    # 匹配不到
    result = re.match("abc", "cdeaabc")
    print(result)
    # search是从整个字符串匹配
    result = re.search("abc", "cdeaabc")
    print(type(result))
    print(result)
    # findAll是从整个字符串中查找匹配
    result = re.findall("abc", "abcdddabcdddaddc")
    print(result)
    # finditer和findAll类似，但返回一个迭代器
    result = re.finditer("abc", "abcdddabcdddaddc")
    print(type(result))
    for result_str in result:
        print(result_str)
    # 使用groups
    result = re.match(r"(\d+)\.(\d+)", "24.1632")
    print(result.groups()[1])
    print(type(result))


def test_replace():
    """
    对检索和替换进行验证
    :return:
    """
    strA = '123abc456bbb'
    result = re.sub(r'\d+', 'A', strA)
    print(result)


def test_split():
    """
    对正则表达式分割字符串进行验证
    :return:
    """
    # 不使用分组的方式。
    strA = '123abc456c789dd102'
    result = re.split(r'[a-z]+', strA)
    print(result)
    # 使用分组的方式，保留分隔符
    result = re.split(r'([a-z]+)', strA)
    print(result)
    # 使用分组不保留分割符
    result = re.split(r'(?:[a-z]+)', strA)
    print(result)


def test_compile():
    """
    对Python的预编译进行验证
    :return:
    """
    strA = '133abc345cde456a'
    pattern = re.compile('([a-z]+)')
    result = pattern.findall(strA)
    print(result)


if __name__ == '__main__':
    test_compile()
