#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author : Echo
# @Time : 2020/7/23 下午4:11
import pytest

def setup_module():
    print('setup_module这个是在每个测试用例执行前执行')
def teardown_module():
    print('teardown_module这个是在每个测试用例执行后执行')
def setup_function():
    print('setup_function这个是在每个测试用例执行前执行')
def teardown_function():
    print('teardown_function这个是在每个测试用例执行后执行')

def test_01():
    print('test_01')
def test_02():
    print('test_02')
def test_03():
    print('test_03')
class Testone:
    def setup(self):
        print('setup这个是在每个测试用例执行前执行')

    def teardown(self):
        print('teardown这个是在每个测试用例执行后执行')
    def setup_class(self):
        print('setup_class这个是在所有测试用例执行前执行')

    def teardown_class(self):
        print('teardown_class这个是在所有测试用例结束后执行')

    def test_01(self):
        print('test_01')

    def test_02(self):
        print('test_02')

    def test_03(self):
        print('test_03')
