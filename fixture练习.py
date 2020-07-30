import pytest


#基础知识练习：
#定一个装饰器函数
@pytest.fixture()
def before():
    print('\每个用例前运行')
#在函数中调用
@pytest.mark.usefixtures('before')
def test01(before):
    print('test01')
@pytest.mark.usefixtures('before')
def test02(before):
    print('test02')
#封装在类中的函数调用
class Test01:
    @pytest.mark.usefixtures('before')
    def test_001(self):
        print('test_001')

    @pytest.mark.usefixtures('before')
    def test_002(self):
        print('test_002')
#在类前面
@pytest.mark.usefixtures('before')
class Test02:
    def test_001(self):
        print('test_001')
    def test_002(self):
        print('test_002')