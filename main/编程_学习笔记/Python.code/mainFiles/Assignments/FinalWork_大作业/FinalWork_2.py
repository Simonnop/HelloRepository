import matplotlib.pyplot as plt

def GetList(num,list):
    return [i[num] for i in list]

def func1(dot):
    return (dot[0]-avg(list_y))*(dot[1]-avg(list_x))

def func2(dot):
    return (dot[1]-avg(list_x))**2

def avg(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    return sum/len(list)

def Sigma(func,list):
    sum=0
    for i in range(len(list)):
        sum+=func(list[i])
    return sum

salaries_and_tenures=[(83000, 8.7),(88000, 8.1),(48000, 0.7),(76000, 6),(69000, 6.5),(76000, 7.5),(60000, 2.5),(83000, 10),(48000, 1.9),(63000, 4.2)]

list_x=GetList(1,salaries_and_tenures)
list_y=GetList(0,salaries_and_tenures)

m_top=Sigma(func1,salaries_and_tenures)
m_bottom=Sigma(func2,salaries_and_tenures)
m=m_top/m_bottom

b=avg(list_y)-m*avg(list_x)

lineDot_x=[x for x in range(11)]
lineDot_y=[x*m+b for x in range(11)]
plt.plot(lineDot_x,lineDot_y,linestyle=':',color='r')
plt.scatter(list_x,list_y)
plt.show()