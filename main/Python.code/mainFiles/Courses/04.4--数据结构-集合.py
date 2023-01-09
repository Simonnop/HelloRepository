'''
    集合 Set

        集合中的元素是互异的

        集合中的检索比列表更快

        声明:
            集合名={值1,值2,...}
        声明空集合:
            集合名=set()
        
        方法:
            .add(添加值)
                向集合中添加值
            .intersection(Set2)
                求交集
            .union(Set2)
                求并集
'''

x={1,2,3,4}
x.add(5)
x
y={2,3,4,5}
x.intersection(y)
x.union(y)

'''
    将列表转换为集合:
        集合名=set(列表名)
'''