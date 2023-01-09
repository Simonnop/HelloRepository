import matplotlib.pyplot as plt

# 保存路径
# plt.savefig(r'目录到文件名')

# 其他方法
# .title(标题)
# .ylabel(y轴名称)
# .xlabel(x轴名称)

'''
    折线图

    按顺序打点,按顺序用线连接
'''
# 调用折线图,参数: x轴,y轴
# marker: 把点打出,可选 x与 o
years=[1950,1960,1970,1980]
gdp=[300,350,500,670]
plt.plot(years,gdp,marker='o',linestyle='--',color='black')
plt.show()


'''
    条形图,直方图
'''
name=['Tom','Tim','Sam']
time=[3,2,4]
# 参数: x,y轴
# range(len())来转换名字为数字,才能被顺序读取绘图
plt.bar(range(len(name)),time,width=0.6,color='green')
# 给x轴项目打上标签: 值与名称相对应
plt.xticks(range(len(name)),name)
plt.show()

# 条形图偏移:见screenshot
# 也可以用列表推导进行加一个数

# 调整统计图坐标范围
# plt.axis([min_x,max_x,min_y,max_y])
plt.axis([-5,105,0,5])
# x,y坐标分隔相同
plt.axis('equal')

'''
    图例
'''
variance=[1,2,4,8,16,32,64,128,256]
bias_squared=[256,128,64,32,16,8,4,2,1]
total_error=[x+y for x,y in zip(variance,bias_squared)]
# 取 variance角标作为 x点
xs=[i for i,_ in enumerate(variance)]
# x点,y点,线的样式,label
plt.plot(xs,variance,'g-',label='variance') # green solid line
plt.plot(xs,bias_squared,'r-.',label='bias^2') # red dot-dashed line
plt.plot(xs,total_error,'b:',label='total error') # blue dotted line
# 设置图例位置
plt.legend(loc=9)
plt.show()

'''
    散点图
'''
id=[1,2,3]
time=[3,2,4]
name=['Tom','Tim','Sam']
# 散点图调用
plt.scatter(id,time)
# 在点上打名字: .annotate(标签,xy=(x坐标,y坐标))
# 一次只能打一个点的标签
for x,y,z in zip(id,time,name):
    plt.annotate(z,xy=(x,y))
plt.show()

'''
    子图
'''
# 先设置一个大图
fig=plt.figure()
# 声明子图并添加进大图
axes1=fig.add_subplot(1,2,1)
axes2=fig.add_subplot(1,2,2)
# 后面就是正常的设置图
# axes1.bar(...)
# axes2.plot(...)
plt.show()

'''
    箱型图

    黄线: 平均数

    箱子顶: 75%
    箱子底: 25%

    白点: 离群值(超过盒子两端1.5倍)
    (可以有方法更改设置)

    顶杠: 群内最大值
    底杠: 群内最小值
'''
import random

class1=[random.gauss(60,15) for _ in range(50)]
class2=[random.gauss(80,5) for _ in range(50)]
plt.boxplot([class1,class2],labels=['Class 1','Class 2'])
plt.show()

'''
    三维作图
'''
# 见screenshot




