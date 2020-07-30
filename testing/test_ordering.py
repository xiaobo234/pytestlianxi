#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author : Echo
# @Time : 2020/7/23 下午3:42
import pytest

#用标签的方式来确定用例执行的顺序
@pytest.mark.run(order=2)
def test_01(login):
    print('test_01')
@pytest.mark.three
def test_02():
    print('test_02')
@pytest.mark.first
def test_03(login):
    print('test_03')
def test_04():
    print('test_04')
def test_05():
    print('test_05')
