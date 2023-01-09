import random

nums=1000000

# 答案推荐
# random.uniform(-1,1)
# uniform方法:在-1与1间随机取小数

randomList_x=[random.randrange(-1000,1001) for _ in range(nums)]
randomList_y=[random.randrange(-1000,1001) for _ in range(nums)]

numList_x=[x/1000 for x in randomList_x]
numList_y=[x/1000 for x in randomList_y]

inTimes=0

for x,y in zip(numList_x,numList_y):
    if (x**2+y**2)<=1:
        inTimes+=1

4*inTimes/nums

