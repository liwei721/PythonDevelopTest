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
    # 复制fileA.txt，生成fileB.txt，注意fileB.txt可以不存在，会自动创建。
    shutil.copyfile("fileA.txt", "fileB.txt")
    # 通过打印文件的属性，可以看出fileA与fileB是
    print(os.stat("fileA.txt"))
    print(os.stat("fileB.txt"))
    # 直接对文件内容复制，参数是Writer对象
    file1 = open("1.txt", encoding="utf-8")
    file2 = open("2.txt", "w", encoding="utf-8")
    shutil.copyfileobj(file1, file2)
    # copy文件的属性信息
    shutil.copystat("fileA.txt", "1.txt")
    print(os.stat("fileA.txt"))
    print(os.stat("1.txt"))
    # copy文件和权限
    shutil.copy("fileA.txt", "3.txt")
    print(os.stat("fileA.txt"))
    print(os.stat("3.txt"))


if __name__ == '__main__':
    test_copy_file()
