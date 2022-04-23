# 2.25 字符串

'''
    字符串
        - 可以使用单引号与双引号标注分隔(但需要配对)
        - 可使用三重单引号,生成多行的字符串

    特殊字符编码(转义字符)
        - 用反斜杠 \+字母 来表示
        - 如 \t 表示tab 
             \n 表示换行
             \' 表示单引号
        - 若就是想打印其本身,使用命令 r''
'''

a='this is\t\'Data\' Science \nClass'
b=r'this is\t\'Data\' \nScience'
c='''第一行
第二行
第三行'''
print(a)
print(b)
print(c)

'''
    len() 计算字符串长度
        - 转义字符长度为 1
        - 空格的长度也会计入(包括句末的空格)
'''

'''
    格式化字符串
        方法一
            - 引号内用 {} 花括号留空
                内部可以限定变量名
                内部可以限定精度,如 {0:.3f} 是保留三位小数
            - 引号外用 .format函数 填入变量
                默认按顺序填入
                也可以根据变量名指定
        方法二
            - 变量写引号外
            - 逗号连接
'''

myAge=20
myName='Tim'
print('{} was {} years old when he wrote this book'.format(myName,myAge))
print('{name} was {age} years old when he wrote this book'.format(name=myName,age=myAge))

print('{0:.3f}'.format(160/9))

age=40
print(myName,'is',myAge,'years old now')

'''
    输入 
        - 使用 input() 函数
        - 括号内为提示语
        - 默认输入为 字符串型 变量
            若想改变,在input前写上数据类型(int float ...)
'''

x=(input("please input x: "))
y=int(input("please input y: "))
print(type(x))
print(type(y))

'''
    \ 换行连接符
'''