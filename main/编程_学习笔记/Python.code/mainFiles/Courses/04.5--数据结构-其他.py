'''
    真值 Truthiness

    含有: False True None

    空列表,空字典,空集合,None, 0 , 0.0  
    以上全都为 False

    is与==的区别:
        is 比较地址相同
        == 比较值相同
'''

x=y={1,2,3}
z={1,2,3}

#  id()函数:显示地址
id(x)
id(y)
id(z)

#  == 比较值
x==y==z
#  is 比较地址
x is z
x is y

'''
    断言语句 assert ... ,'错误内容字符串'

    若 assert 后的语句为假
    则会抛出错误 AssertionError
'''

a=0
assert a>5,'a必须大于5'

'''
    all函数 any函数

    all() 函数的输入是一个列表
    只有当列表中每一个都不为 False 时才返回 True

    any() 函数的输入是一个列表
    只有当列表中至少有一个为 True 时才返回 True

    all([]) 为 True 是因为列表中没有为"False"的元素

    any([]) 为 False 是因为列表中没有为"True"的元素
'''



