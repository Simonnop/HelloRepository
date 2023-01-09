# 3.11 字典

'''
    字典是一个接一个的键值对

    声明:
        字典名={键1:值1,键2:值2,键3:值3,...}
    声明空字典:
        字典名={}
        字典名=dict()

    查找:
        字典名[键x]

    修改/添加(键存在则修改,不存在则添加):
        字典名[键x]=值x

    方法
        .get()
            查询键的值 .get(键x,(默认值))
            查询不到则不会报错,会返回默认值(默认为None)
        .keys()
            取出所有键的值
            类型为 dict_keys
            可以用 list() 来变为列表
        .values()
            取出所有值的值
            类型为 dict_values
            可以用 list() 来变为列表
        .items()
            取出所有键值对
            类型为 dict_items
    
    查询
        值x/键x in 字典名
        默认查询为键,若查询值则加方法.values()
        返回类型为Bool
'''

grade={'Tim':90,'Kate':98}
grade

# 查找
grade['Tim']

# 修改/添加
grade['Kate']=96
grade['Sam']=89
grade

# .get() 方法
grade.get('Mike','NOT FOUND')
x=grade.get('Simonnop')
type(x)

# .keys() 方法
# .values() 方法
grade.keys()
list(grade.keys())
list(grade.values())

for i in grade.keys():
    print(i)

# .items() 方法
y=grade.items()
type(y)
# dict_items 被 print 出来的是元组
for i in y:
    print(i)

'''

    默认字典 defaultdict

        默认字典查一个不存在的东西不会报错
        会自动创建一个键,并依据方法赋予一个返回值

        引入:
            from collections import defaultdict
        声明:
            字典名=defaultdict(方法)
        方法:
            int   返回为 0
            list  返回空列表
            dict  返回空字典

    字典也可以与列表,元组相互嵌套
'''

from collections import defaultdict
from enum import EnumMeta
from typing import Counter
x=defaultdict(int)
x['Tim']
x['Sam']+=1
x

'''
    计数器 Counter

        引入:
            from collections import counter
        声明:
            x=counter(被查找的列表)
        方法:
            .most_common() 
            按照出现的次数排序输出(输出列表嵌套元组)

'''

from collections import Counter
x=Counter([0,2,2,1,3,5,4,4,4,'nb','sb','nb'])
x
x.most_common()

'''
    枚举 
    for循环中使用枚举,会取出它的角标
'''
name=['Tom','Tim','Sam']
for i,name in enumerate(name):
    print('name',i,'is',name)


