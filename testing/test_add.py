#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author : Echo
# @Time : 2020/7/23 下午2:39
import pytest

def test_01():
    print('test_01')

def test_02():
    print('test_02')

def test_03():
    print('test_03')
def test_04():
    print('test_04')
def test_05():
    print('test_05')
@pytest.fixture()
def get_10():
    return 10
def test_fiture(get_10):
    print(get_10)