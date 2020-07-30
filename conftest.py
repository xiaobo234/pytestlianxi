#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author : Echo
# @Time : 2020/7/23 下午7:09
import pytest

#所有配置数据
@pytest.fixture(scope='session')
def login():
    print('我是conftest配置文件')
    yield
    print('执行teardowsn！')#如果用例异常，也不影响teardown的执行，运行结果互不影响，如果setup就失败了，那么就不会执行yield'后面的