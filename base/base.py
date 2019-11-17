# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:
"""
from datetime import datetime
import os
import pytest
import allure
import argparse


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(PROJECT_DIR, "output")

def save_screenshot(self, img_doc):
    '''
    页面截屏保存截图
    :param img_doc: 截图说明
    :return:
    '''
    file_name = OUTPUTS_DIR + "\\{}_{}.png".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"), img_doc)
    self.driver.save_screenshot(file_name)
    with open(file_name, mode='rb') as f:
        file = f.read()
    allure.attach(file, img_doc, allure.attachment_type.PNG)


def get_arg():
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--gpus', type=str, default="test0")
    parser.add_argument('--batch-size', type=str, default="all")
    args = parser.parse_args()
    print(args.gpus)
    print(args.batch_size)