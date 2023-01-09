'''
    Lambda 匿名函数
        通过单个语句生成函数
        用完就不存在了
    
    语法:
        函数名=lambda 参数:返回语句
'''

from random import random


Func=lambda x:x*2
Func(2)

#  key= 按指定函数排序
x=[1,-4,-3,-5]
#  按负值来排序
x.sort(key=lambda x:-x,reverse=True)

x=[1,-4,-3,-5]
#  按倒数来排序
x.sort(key=lambda x:1/x,reverse=True)
x

'''
    列表推导
        将一个列表以一定的逻辑转化为另一个列表
    
    列表名 = [值 规则 条件 ...]

    常用规则或条件
    for ... in ...
    if ...
'''

x=list(range(1,10))
x

# 将偶数值平方并传入
y=[i**2 for i in x if i%2==0]
y

# 等价写法
z=[]
for i in x:
    if i%2==0:
        z.append(i**2)
z

# 以列表解析创建字典
a={str(x):x**2 for x in range(10)}
a
# 以列表解析创建集合
b={x*x for x in range(-5,5)}
b

# 以常数函数创建,其中_能为任意值
# 可以用此方法限制列表长度
c=[0 for _ in range(10)]
c

# 嵌套 相当于嵌套 for循环
d=[(x,y)
    for x in range(10)
    for y in range(10)]
d

# 创建字母列表:使用 ASCII码函数 chr()
upperLetters=[chr(i) for i in range(65,91)]
upperLetters

'''
    随机数产生

    引入
        import random

    常用
        random.random()
        创建随机数

        random.randrange(开头数,结尾数+1)
        范围内创建随机数

        random.shuffle(列表)
        随机排列列表中的元素

        random.gauss(开头数,结尾数)
        高斯分布

        random.choice(列表)
        一次有放回的随机抽取
            - 多次有放回的随机抽取,可以用 choice + 列表推导

        random.sample(列表,个数)
        任意次无放回的随机抽取
'''

import random

listNum=list(range(10))
random.shuffle(listNum)
listNum

# 正态分布图像

# import matplotlib.pyplot as plt
# import random
# guass=[random.gauss(0,1) for _ in range(10000)]

# 直方图
# hist:直方图  bins:分割  density:频率显示
# plt.hist(guass,bins=50,density=True)
# plt.show()

# 条形图
# plt.bar(x坐标, y坐标 , tick_lable=(参数,写每个条的对应项目名) )
# 例:
# x: range(len( )) y:

