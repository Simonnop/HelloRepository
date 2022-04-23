import csv
import matplotlib.pyplot as plt

filepath=r'C:\Users\admin\OneDrive\Python.code\mainFiles\Assignments\Chapter_7.2_练习\ExamAnxiety.csv'
x=open(filepath,encoding='utf-8')

content=csv.reader(x)
next(content)

Revise=[]
Anxiety=[]
Gender=[]
Revise_M=[]
Revise_F=[]

for i in content:
    Revise.append(int(i[1]))
    Anxiety.append(float(i[3]))
    # 这里假设 1为男, 2为女
    if i[4]=='1':
        Gender.append('男')
        Revise_M.append(int(i[1]))
    else:
        Gender.append('女')
        Revise_F.append(int(i[1]))

plt.scatter(Revise,Anxiety)
plt.xlabel('Revise')
plt.ylabel('Anxiety')
plt.show()

plt.boxplot([Revise_M,Revise_F],labels=['Male','Female'])
plt.show()

