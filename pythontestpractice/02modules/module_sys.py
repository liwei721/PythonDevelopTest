"""
    @author: xuanke
    @time: 2020/6/3
    @function: 对sys模块进行验证
"""
import sys
import shutil


def test_std_method():
    """
    对输入输出进行验证
    :return:
    """
    sys.stdout.write("test python")
    print("please input something")
    input_str = sys.stdin.readline()
    print(input_str)
    sys.stderr.write("throw error")

if __name__ == '__main__':
    test_std_method()
    print(shutil.get_archive_formats())