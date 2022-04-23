from cmath import sqrt
from hashlib import new
import matplotlib.pyplot as plt
import random
import math

guassList=[random.gauss(100,8) for _ in range(100000)]

# 1.计算整个列表的均值与标准差
def Avg(List):
    sum=0
    for i in List:
        sum+=i;
    return sum/len(List)

def Sd(List):
    sum_sd=0
    avg=Avg(List)
    for i in List:
        sum_sd+=(i-avg)**2
    return sqrt(sum_sd/len(List))

Avg(guassList)
Sd(guassList)


# 2.随机抽取100个样本,计算均值与标准差
def GetNewList(List,len):
    newList=[]
    for _ in range(len):
        key=random.randrange(1,100001)
        newList.append(List[key]) 
    return newList

newList=GetNewList(guassList,100)

Avg(newList)
Sd(newList) 

# 3.重复1000次,并绘制直方图
avgList=[]
sdList=[]
for _ in range(10000):
    newList=GetNewList(guassList,100)
    avgList.append(Avg(newList))
    sdList.append(Sd(newList))

plt.hist(avgList,bins=100,density=False)
plt.show()
plt.hist(sdList,bins=100,density=False)
plt.show()



