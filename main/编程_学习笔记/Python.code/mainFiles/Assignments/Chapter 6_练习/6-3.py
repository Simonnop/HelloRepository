import random

def Insist():
    doors=[0,0,1]
    choice=random.randrange(0,3)
    if(doors[choice]==1):
        return True

# 不换胜率
wins=0
times=10000
for _ in range(times):
    if(Insist()):
        wins+=1
wins/times


def Change():
    doors=[0,0,1]
    choice=random.randrange(0,3)
    # 如果选择了第一扇门,则第二扇门会开,换就等同选择第三扇门
    if(choice==0):
        choice=2
    # 如果选择了第二扇门,则第一扇门会开,换就等同选择第三扇门
    elif(choice==1):
        choice=2
    # 如果选择了第三扇门,则剩下的都是山羊
    else:
        choice=0
    if(doors[choice]==1):
        return True

# 换胜率
wins=0
times=10000
for _ in range(times):
    if(Change()):
        wins+=1
wins/times


