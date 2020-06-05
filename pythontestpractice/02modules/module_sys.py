"""
    @author: xuanke
    @time: 2020/5/28
    @function: sys 模块
"""
import sys


def test_dynamic():
    """
    对sys模块的动态对象验证
    :return:
    """
    print(sys.argv)
    print(sys.path)
    print(sys.modules)


def test_static():
    """
    获取sys模块的静态对象
    :return:
    """
    # 获取Python可执行文件的路径
    print(sys.executable)
    # 获取当前操作系统的名称
    print(sys.platform)
    # 获取Python解释器内置的模块。
    print(sys.builtin_module_names)
    # 获取Python解释器的版本信息
    print(sys.implementation)


if __name__ == '__main__':
    test_static()
