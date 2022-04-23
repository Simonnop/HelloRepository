# 3.7 基本数据结构

'''
    面向对象的程序设计

    对象在封装后,拥有数据与方法
'''

s='abcde'

# 首字母大写
s.capitalize()

# 所有大写
s.upper()

# 查找,从0开始
s.find('d')

# 此类方法不改变本身内部数据
s

'''
    列表
        - "列表就是一个接一个的东西放一起",没有类型限制

        - 语法:
            列表名=[元素1,元素2,元素3,...]

        - 方法:
            L:列表  e:元素

            添加 
                .append(e)    
            排序 
                .sort()   
                参数选择: reverse=True 倒序
            拼接 
                .extend(L)    
                更改自身,不想改变直接用加号 L1+L2
            插入
                .insert(i,e)  在i位置插入元素
            拆分
                .split()
                可以将字符串拆分为列表(以空格为界)
                参数选择: sep='x' 拆分时除去
            聚合
                'x'.join(L)
                可以将列表聚合为字符串
                'x' 为元素间的连接

        - 索引
            列表名[角标]
            角标为正数为从前往后数,为负数为从后往前数
            选择多个 [首个:末个+1] (不写则默认该方向所有)

        - 删除
            del 删除项
            del可以删除之前定义的函数,以使用对象内封装的方法

        - 列表可以嵌套(多层角标来索引),可以为空
        
        - 列表的复制(切取)
            - 列表的复制不能直接写 y=x 
              这样是传递地址,不是复制,修改一个会使两个都会变化
            - 正确复制操作:
                y = x[:]

        - 判断是否在列表
            元素 in 列表名,返回bool值

        - 值提取
            x,y=L
            接收的变量数必须等于列表内的变量数
            通常用 _ 表示想忽略的变量
'''

# 创建列表
shoplist=['apple','banana','orange']
shoplist2=[]

# 列表长度
print("the length is",len(shoplist))

# 遍历
for item in shoplist:
    print(item)

# 添加
shoplist.append('egg')

# 排列
shoplist.sort()

# 索引
shoplist[0]
shoplist[-2:]
shoplist[2:3]

# 删除
del shoplist[0]

# 修改某个值
shoplist[1]='rice'

# 复制
shoplist2=shoplist[:]

# 判断是否在列表
'hamburger' in shoplist

# 值提取
_,x,y,_=shoplist
print(x,y)

# 聚合
' or '.join(shoplist) 