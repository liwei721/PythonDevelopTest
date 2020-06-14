"""
    @author: xuanke
    @time: 2020/5/28
    @function: 对util模块进行验证
"""
import shutil
import os


def test_copy_file():
    """
    对拷贝文件进行验证
    :return:
    """
    # 复制fileA.txt，新创建1.txt。
    file_1 = shutil.copyfile("fileA.txt", "1.txt")
    print(file_1)

    # 创建一个2.txt的文件
    file1 = open("1.txt", encoding="utf-8")
    file2 = open("2.txt", "w", encoding="utf-8")
    print(type(file2))
    shutil.copyfileobj(file1, file2)
    # copy文件的权限信息
    shutil.copymode("fileA.txt", "2.txt")
    # 主要查看文件元祖数据中的std_mode
    print(os.stat("fileA.txt"))
    print(os.stat("2.txt"))

    # copy文件的权限位、最近访问时间、最近修改时间
    shutil.copystat("fileA.txt", "2.txt")
    print(os.stat("fileA.txt"))
    print(os.stat("2.txt"))

    # copy文件和权限
    shutil.copy("fileA.txt", "test/")


def test_operate_folder():
    """
    验证对folder的操作
    """
    return_folder = shutil.copytree(".", "testB", ignore=shutil.ignore_patterns('*.pyc', '*.txt'))
    print(return_folder)

    shutil.rmtree("testA")

    return_value = shutil.move("test", "testC")
    print(return_value)


def test_archive_folder():
    """
    对文件进行归档和解包
    :return:
    """
    # 压缩
    file_name = shutil.make_archive("test", "zip", base_dir=".")
    print(file_name)
    # 解压
    shutil.unpack_archive("test.zip", "mytest", "zip")


if __name__ == '__main__':
    test_archive_folder()
