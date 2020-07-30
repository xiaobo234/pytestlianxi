#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author : Echo
# @Time : 2020/7/27 下午8:08
import pytest

@pytest.fixture(scope='module', autouse=True)
def module1():
    print('\n开始执行module')
@pytest.fixture(scope='class')
def class2():
    print('\n开始执行class')
@pytest.fixture(scope='function', autouse=True)
def function1():
    print('\n开始执行function')
def test_a():
    print('---用例a执行---')
def test_d():
    print('---用例d执行---')

class TestCase1:
    def test_b(self):
        print('---用例b执行---')
    def test_c(self):
        print('---用例c执行---')

@pytest.fixture(scope='class')
def test1():
    b = '男'
    print('传出了%s, 且只在class里所有用例开始前执行一次！！！' % b)
    return b
def test_01(test1):
    print('这个是个函数')

class TestCase:
    def test3(self, test1):
        name = '男'
        print('找到name')
        assert test1 == name

    def test4(self, test1):
        sex = '男'
        print('找到sex')
        assert test1 == sex

