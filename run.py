# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:
"""

import pytest
import os
import sys, getopt

def main(argv):
    inputfile = ""
    outputfile = ""

    try:
        # 这里的 h 就表示该选项无参数，i:表示 i 选项后需要有参数
        opts, args = getopt.getopt(argv, "hi:o:", ["infile=", "outfile=", "version", "help"])
        # 第一个是 (option, value) 元组的列表。 第二个是参数列表，包含那些没有'-'或'--'的参数
    except getopt.GetoptError:
        print('test_arg.py -i <inputfile> -o <outputfile>')
        print('or: test_arg.py --infile=<inputfile> --outfile=<outputfile>')
        print('or: test_arg.py --version --help')
        sys.exit(2)

    if len(args) > 0:  # 表示有未识别的参数格式
        print('test_arg.py -i <inputfile> -o <outputfile>')
        print('or: test_arg.py --infile=<inputfile> --outfile=<outputfile>')
        print('or: test_arg.py --version --help')
        sys.exit(1)
    else:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print('test_arg.py -i <inputfile> -o <outputfile>')
                print('or: test_arg.py --infile=<inputfile> --outfile=<outputfile>')
                print('or: test_arg.py --version --help')

                sys.exit()
            elif opt in ("-i", "--infile"):
                inputfile = arg
            elif opt in ("-o", "--outfile"):
                outputfile = arg
            elif opt in ("--version"):
                print('0.0.1')
                sys.exit()

    print('Input file : ', inputfile)
    print('Output file: ', outputfile)

import argparse
def get_arg():
    parser = argparse.ArgumentParser(description="自定义python命令行参数")
    parser.add_argument('--env', type=str, default="test0")
    parser.add_argument('--project', type=str, default="all")
    parser.add_argument('--port', type=str, default="all")
    args = parser.parse_args()
    print(args.env)
    print(args.project)
    print(type(args))

# global arg
# arg = {
#     "--env": "test0",
#     "--project": "all",
#     "port": "pc",
#     "pattern": 0, # 0-本地执行，1-开启分布式
# }

if __name__ == '__main__':
    # main(sys.argv[1:])
    get_arg()


    # pytest.main(["-sq",
    #              "--alluredir", "./allure-results"])
    # os.system(r"allure generate --clean allure-results -o allure-report")

# try:
#     options, args = getopt.getopt(sys.argv[1:], "ho:i:", ["help", "ip=", "port="])
# except getopt.GetoptError:
#     print
# 'hi Sam getopt error!Please input -h or --help'
# sys.exit(1)
#
# for name, value in options:
#     if name in ("-h", "--help"):
#         usage()
#         print
#         ""
#     elif name in ("-o", "-i"):
#         print
#         "short  parameter %s" % (value)
#     elif name in ("--ip", "--port"):
#         print
#         "long  parameter %s" % (value)
#
# for item in args:
#     print
#     item