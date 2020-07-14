import pytest
import pytest_ordering

#有两种运行方式，一是python解释器，一种是pytest解释器
#方式一：直接配置python解释器，然后加入口，如下：
def fun(a):
    return a+1
@pytest.mark.parametrize('a,b',[(1,2),(3,4)]) #装饰器+参数化
def test_001(a,b):
    assert fun(a)==b
def test_002():
    assert fun(3)==4
def test_003():
    assert fun(4)==5

class Test():
    @pytest.mark.run(order=2)
    def test_01(self):
        print('a')
    @pytest.mark.run(order=1)
    def test_02(self):
        print('b')
if __name__=='__main__':
    pytest.main(['test.py']) #用python解释器运行pytest脚本的入口，用pytest解释器时，无需入口

# #方式二：直接用pytest解释器，无需入口
# def fun(a):
#     return a+1
# def test_001():
#     assert fun(2)==3