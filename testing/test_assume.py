#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author : Echo
# @Time : 2020/7/21 下午7:31
import sys
import pytest_assume #多重校验，断言失败后下一个断言照样可以正常执行。
import pytest
sys.path.append('..')
from pythoncode.calc import Calcu

#  多重校验（assume）和失败重跑（rerun）

class Test_calc:
    @pytest.fixture()
    def add_cal(self):
        self.add = Calcu()
    @pytest.fixture()
    def div_cal(self):
        self.div=Calcu()
    #计算器加法运算
    def test_add(self,add_cal):
        # print('断言1')
        # assert 3==self.add.add(1,2)
        # print('断言2')
        # assert 3 == self.add.add(1, 3)
        # print('断言3')
        # assert 4 == self.add.add(2, 2)
        #以下代码是：即多重校验，断言失败后下一个断言照样可以正常执行。
        print('断言1')
        pytest.assume(3 == self.add.add(1, 2))
        print('断言2')
        pytest.assume(3 == self.add.add(1, 3))
        print('断言3')
        pytest.assume(4 == self.add.add(2, 2))
    #计算器除法运算
    @pytest.mark.flaky(reruns=5,reruns_delay=1)#当用例执行失败时，指定可以测试用例执行的最大次数
    def test_div(self,div_cal):
        assert  2==self.div.div(6,2)
    #也可以用命令行执行，pytest  --retun 5

