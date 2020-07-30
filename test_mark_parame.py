import pytest

'''
标记函数参数化（测试用例方法前加测试数据）：@pytest.mark.parametrize("a,b,expected", testdata)
语法：
ep1　传入单个参数
@pytest.mark.parametrize('参数名',lists)
ep2 传入两个参数
@pytest.mark.parametrize('参数1','参数2',[(
参数1_data[0],参数2_data[0]),(参数1_data[1],参数2_data[1])]
传三个或者更多也是这样传。list的每个元素都是一个元祖，元祖里的每个元素和按参数顺序一一对应。
'''
#传入两个参数
@pytest.mark.parametrize('test_input,expected',[('3+5',8),('2+4',6),("6*9",42)])
def test_eval(test_input,expected):
    assert eval(test_input)==expected
#参数结合
@pytest.mark.parametrize('x',[0,1])
@pytest.mark.parametrize('y',[2,3])
def test_foot(x,y):
    print("测试数据结合：x=%s,y=%s"% (x, y))

# 传一个参数
@pytest.mark.parametrize('task',['a',1,2])
def test_add_4(task):
    print(task)






