"""
    @author: xuanke
    @time: 2020/5/10
    @function: 验证Python中的基本数据结构
"""
import sys
import os
import urllib.request


def test_dict():
    """
    验证对字典进行遍历
    :return:
    """
    test_dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict_keys = test_dict1.keys()
    for key in dict_keys:
        print(key)
        print(test_dict1.get(key))


def test_fibonacci(n):
    """
    验证生成器，打印斐波那契数列
    :param n:
    :return:
    """
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


def test_if(score):
    """
    验证if控制语句
    :return:
    """
    if score < 0:
        print('成绩无效')
    elif score < 60:
        print('成绩不及格')
    elif score < 90:
        print('良好')
    else:
        print('优秀')


def test_sum():
    """
    使用while循环求1到100的和
    :return:
    """
    counter = 1
    number = 0
    while counter <= 100:
        number = number + counter
        counter += 1
    print(number)


def test_sum_for():
    """
    使用for循环求1到100的和
    :return:
    """
    number = 0
    for counter in range(101):
        print(counter)
        number = number + counter
    print(number)


def test_break():
    """
    验证break语句
    :return:
    """
    name_list = ['TOM', 'lilei', 'JACK', 'Feng']
    for name in name_list:
        if 'TOM' == name:
            print('find TOM')
            break
        else:
            print(name)
    print('is end')


def test_continue():
    """
    验证continue语句
    :return:
    """
    name_list = ['TOM', 'lilei', 'JACK', 'Feng', 'TOM']
    age = 0
    for name in name_list:
        if 'TOM' != name:
            print('no TOM continue')
            continue
        if age == 24:
            print('find TOM')
    print('is end')


def test_write_file():
    """
    向文件test.txt中写入内容
    :return:
    """
    with open("test.txt", 'w+') as file_obj:
        file_obj.write("hello world!!")
        file_obj.flush()
        file_obj.close()


def test_read_file():
    """
    向文件test.txt中写入内容
    :return:
    """
    with open("test.txt", 'r+') as file_obj:
        read_content = file_obj.readline()
        print(read_content)
        file_obj.close()


def test_rename_file():
    """
    向文件test.txt中写入内容
    :return:
    """
    os.rename("test.txt", "hello.txt")


def test_remove_file():
    """
    验证删除一个文件
    :return:
    """
    os.remove("hello.txt")


def test_mkdir():
    """
    创建单个目录
    :return:
    """
    os.mkdir("test")


def test_mkdirs():
    """
    创建单个目录
    :return:
    """
    os.makedirs("test/test1/test2")


def test_rmdir():
    """
    创建单个目录
    :return:
    """
    os.rmdir("test/test1/test2")
    os.removedirs("test/test1")


def test_urllib_get():
    url = "https://api.apiopen.top/getJoke?page=1&count=2&type=video"
    resp = urllib.request.urlopen(url)
    print(resp.read())


def test_urllib_post():
    url = "https://api.apiopen.top/getJoke?page=1&count=2&type=video"
    resp = urllib.request.urlopen(url, data=b"")
    print(resp.read())


if __name__ == '__main__':
    # test_write_file()
    # test_urllib_get()
    test_mkdirs()