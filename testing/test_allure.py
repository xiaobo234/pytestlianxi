#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author : Echo
# @Time : 2020/7/29 下午11:30

#测试报告练习
import allure
import pytest

@allure.feature('allure练习')
def test_1():
    print('test01')
def test_2():
    print('test02')
def test_3():
    print('test03')
def test_4():
    print('test04')
def test_5():
    assert 4==6