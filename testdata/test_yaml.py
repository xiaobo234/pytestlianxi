#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author : Echo
# @Time : 2020/7/28 下午7:30
import pytest
import yaml
import allure

# 从data.yml 中读取数据
@allure.feature('读取数据的功能')
# @pytest.mark.parametrize('a,b',yaml.safe_load(open("data.yml")))
# #@pytest.mark.parametrize('a,b',[(1,2),(3,4)])
# def test_foo(a,b):
#     print(yaml.safe_load(open("data.yml")))
#     print(f'a+b={a+b}')
def test_1():
    print('这是个测试报告')


