"""
    @author: xuanke
    @time: 2020/5/28
    @function: os 模块
"""
import os
import time


def test_folder():
    """
    创建目录验证
    :return:
    """
    # 1.创建单个目录
    os.mkdir("test")
    # 2. 递归创建目录
    os.makedirs("test/test1/test2")
    # 3. 重命名目录
    os.rename("test/test1/test2", "test/test1/test3")
    # 4. 递归重命名目录
    os.renames("test/test1/test3", "test1/test2/test4")
    # 5. 删除某个目录
    os.rmdir("test1/test2/test4")
    # 6. 递归删除某个目录
    os.removedirs("test1/test2")


def test_scan_folder():
    """
    验证对目录遍历
    :return:
    """
    # 1.先递归创建目录
    os.makedirs("test/test1/test2/test3")
    # 2. 遍历目录
    list_dir = os.listdir("test")
    print(list_dir)
    # 3. 递归遍历目录
    walk_dir = os.walk("test")
    print(walk_dir)
    for parent, dir_name, file_name in walk_dir:
        # 注意 dir_name和file_name返回的都是列表。
        print(parent)
        print(dir_name)
        print(file_name)
    # 4. 遍历目录
    scan_dir = os.scandir("test")
    print(scan_dir)
    for dir_name in scan_dir:
        # dir_name是一个Entry对象
        print(dir_name.name)


def test_file_attribute():
    """
    验证文件属性方法
    :return:
    """
    file_a = os.open("fileA.txt", os.O_CREAT | os.O_RDWR)
    os.write(file_a, b"test python os")
    os.close(file_a)
    file_stat_a = os.stat("fileA.txt")
    print(file_stat_a)
    # 返回的是一个时间戳
    file_mtime_a = os.path.getmtime("fileA.txt")
    print(file_mtime_a)
    # 将时间戳格式化成可识别的时间字符串
    format_time_a = time.ctime(file_mtime_a)
    print(format_time_a)
    # 获取文件大小，单位是KB
    file_size_a = os.path.getsize("fileA.txt")
    print(file_size_a)


def test_open():
    """
    验证with open方式
    :return:
    """
    with open("fileA.txt", "w+") as f1:
        f1.write("test python")


def test_path():
    """
    对路径操作的验证
    :return:
    """
    # 获取当前工作目录
    print(os.getcwd())
    # 返回的是相对路径的上级目录，其实就是..
    print(os.pardir)
    # 获取目录testA的绝对路径，这个比较常用。
    print(os.path.abspath("testA"))
    # 获取目录testA所在的目录，其实就是上级目录，注意dirname方法的参数需要是绝对路径。它经常和abspath方法配合使用。
    print(os.path.dirname(os.path.abspath("testA")))
    # 判断一个路径是否是绝对路径
    print(os.path.isabs("testA"))
    # 对路径做拼接，这个也比较常用，可以避免直接使用+进行拼接，在windows和linux上会有兼容性问题。
    print(os.path.join(os.getcwd(), "testA"))
    # 对路径分割，效果可以参考运行结果。返回一个元组
    print(os.path.split(os.path.abspath("testA")))
    # 如果文件有后缀，则将文件分割成后缀和路径，返回一个元组
    print(os.path.splitext(os.path.abspath("fileA.txt")))


def test_system():
    """
    对系统操作进行验证
    :return:
    """
    s_result = os.system("cd testA")
    print(s_result)
    p_result = os.popen("ping www.baidu.com")
    print(p_result.read())
    print(os.getpid())
    print(os.uname())
    print(os.environ())

if __name__ == '__main__':
    test_system()
