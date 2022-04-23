'''
    类 class

    我们通过使用 class 语句与这个类的名称来创建一个新类。
    在它之后是一个缩进的语句块，代表这个类的主体。

    类的调用    
        对象 = person(对象名)
    
'''


class Person:
    def say_hi(self):
        print('Hello, how are you?')


p = Person()
p.say_hi()

# 前面两行同样可以写作
# Person().say_hi()

'''
    self:
        调用类的对象名,即要生成的对象

    __init__ 方法

        用于初始化,设置 self 的属性(数据结构)
        __init__ 方法中一定要有 self 参数
        __init__ 方法中可以任意添加 self 的属性
'''


class Person:
    def __init__(self, name):
        self.name = name
        self.age = None

    def add_Age(self, age):
        self.age = age

    def say_hi(self):
        print('Hello, my name is', self.name, '\nI am', self.age, 'years old')


# 向类添加对象
p = Person('Swaroop')

p.add_Age(18)
p.say_hi()

# 尝试自己设置 Set 类
class Set:
    def __init__(self, values=None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        # __repr__ 一定要使用 return 来返回类型
        return '('+str(list(self.dict.keys()))+')'

    def add(self, value):
        # 没有实际意义,只是为了凑够键值对的值
        self.dict[value] = True

    def contains(self, value):
        # return一个 Bool 值
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

s=Set([1,2,3])
s

'''
    类方法

    书写类方法时，在上一行先写装饰器
        @classmethod
    
    函数中的参数是 cls
    
    cls 可以调用类中声明的对象

    调用方法
        cls.类中变量
'''

# 一个类变量，用来计数机器人的数量
class Robot:
    # 表示有一个带有名字的机器人
    population = 0
    
    def __init__(self, name):
        # 初始化数据
        self.name = name
        print("(Initializing {})".format(self.name))
        # 当有人被创建时，机器人将会增加人口数量
        Robot.population += 1

    def die(self):
        # 我挂了
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        # 来自机器人的诚挚问候
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        # 打印出当前的人口数量
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")

droid1.die()
droid2.die()
Robot.how_many()






