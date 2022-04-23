'包是模块的集合,模块是函数的集合'

'''
    声明函数
        语法
            def 函数名(参数):
                ...
            - 参数可以设置默认值
    
    执行函数
        语法
            函数名(参数)
            - 若参数未输入,则以默认值执行
            - 可以不指定参数名来设置值,则会依照顺序给参数传递值
'''

def print_Sum(a=1,b=2):
    print('the sum of {} and {} is {}'.format(a,b,a+b))

print_Sum()
print_Sum(3,5)
print_Sum(2,b=4)

'''
    DocString 文档字符串
        - 给函数增加说明文档
        - 用法: 在函数开头直接以字符串写入即可

    使用 help() 函数可以被查询
'''

def say_Hello():
    '这个函数可以跟你说Hello'
    print('Hello!')

help(say_Hello)

'''
    模块
        - 模块是一系列函数的集合,以文件的形式存放在特定的目录下
        - 模块一般是一个.py文件
        - 模块在本文件工作路径下可以直接使用
        - 外部模块在导入后才可以直接使用其内的函数
        - 导入语法
            1. from 模块名 import 函数
                - 这样写可以直接使用函数
                - 导入模块内的所有函数:  from 模块名 import *
            2. import 模块  
                - 使用函数则需要写: 模块名.函数
                - 此方法更加常用
        - 更改模块名
            import 模块名 as 新模块名
'''

# 查找工作路径
import os
os.getcwd()

# 改变工作路径
# import os
# os.chdir(工作路径)

# 查找可放置模块的路径
import sys
sys.path

# sys.path.append 添加模块的储存路径
import sys
sys.path.append(r'C:\Users\admin\OneDrive\Python.code\mainFiles\Resource')
import myModule
myModule.say_Hi()

'''
    查看模块内所有函数
        - 使用 dir 函数
        - 语法: dir(模块名)

    删除模块
        - 使用 del 函数
        - 语法: del 模块名
'''

# 查看可运行的所有模块
dir()

import math
dir(math)

'''
    随机数 random
        语法: random.random()
        - 可以设置种子数相同来使生成的随机数相同
        - random.seed(种子数)
        
'''

import random

random.seed(10)
random.random()

random.random()

'''
    包

    建议安装包的路径:
    C:\Program Files\Python310\Lib\site-packages

    包是一种组织模块的方式
    指一个包含模块与 __init__.py 文件的文件夹

    当包被导入时,会执行 __init__.py 内的内容

    若想要执行的模块若在大包的子包内,则需要一级一级导入

    
'''

