# 1.输出23人的生日编号
import random
BirthdayList=[]
for i in range(23):
    a=random.randint(1,365)
    BirthdayList.append(a)
for item in BirthdayList:
    print(item,end=' ')

# 2.判断是否有人生日相同
BirthdaySet=set(BirthdayList)
if len(BirthdayList)==len(BirthdaySet):
    print('\n没有人生日相同')
else:
    print('\n有人生日相同')

# 3.记录生日相同的次数
SameTime=0
for j in range(100000):
    BirthdayList=[]
    for i in range(23):
        a=random.randint(1,365)
        BirthdayList.append(a)

    BirthdaySet=set(BirthdayList)
    if len(BirthdayList)!=len(BirthdaySet):
        SameTime+=1
SameTime
    



