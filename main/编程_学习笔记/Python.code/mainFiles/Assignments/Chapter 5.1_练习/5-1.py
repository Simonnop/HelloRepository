# 尝试自己设置 Set 类
class Set:
    def __init__(self, values=None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

    # def __repr__(self):
    #     print('{', end='')
    #     dictLen = len(self.dict)
    #     for i in self.dict:
    #         if i != dictLen:
    #             print(i, end=',')
    #         else:
    #             print(i, end='')
    #     print('}')
    #     return ''

    # 答案

    def __repr__(self):
        x=str(list(self.dict.keys()))  
        # 将其转化为字符串列表
        # 不打印其首尾的括号  
        return '('+x[1:(len(x)-1)]+')'

    def add(self, value):
        # 没有实际意义,只是为了凑够键值对的值
        self.dict[value] = True

    def contains(self, value):
        # return一个 Bool 值
        return value in self.dict

    def remove(self, value):
        del self.dict[value]


s = Set([1, 2, 3])
s
