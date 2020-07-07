"""
    @author: xuanke
    @time: 2020/7/7
    @function: 命令行参数
"""
import argparse


def init_argparse():
    parse = argparse.ArgumentParser(description="interface cli param")
    parse.add_argument('-ut', '--unit_type', help="unittest type", default='pytest')
    parse.add_argument('-s', '--source', help="testcase path")
    parse.add_argument('-o', "--output", help="test report path")
    parse.parse_args()


if __name__ == '__main__':
    init_argparse()
