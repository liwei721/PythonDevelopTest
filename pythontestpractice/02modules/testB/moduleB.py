"""
    @author: xuanke
    @time: 2020/5/19
    @function: 在moduleB中引用moduleA
"""

import moduleA


def methodB():
    moduleA.test_a()
    print("method B")


if __name__ == '__main__':
    print(globals())
    print(locals())
