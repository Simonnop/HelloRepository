# 1.读取csv
import csv
filepath=r'C:\Users\admin\OneDrive\Python.code\mainFiles\Assignments\Chapter 7_练习\ExamAnxiety.csv'
x=open(filepath,encoding='utf-8')

content=csv.reader(x)
next(content)

Code=[]
Revise=[]
Exam=[]
Anxiety=[]
Gender=[]

for i in content:
    Code.append(int(i[0]))
    Revise.append(int(i[1]))
    Exam.append(int(i[2]))
    Anxiety.append(float(i[3]))
    # 这里假设 1为男, 2为女
    if i[4]=='1':
        Gender.append('男')
    else:
        Gender.append('女')

for i in zip(Code,Revise,Exam,Anxiety,Gender):
    print(i)


# 2.读取诗 txt
filepath=r'C:\Users\admin\OneDrive\Python.code\mainFiles\Assignments\Chapter 7_练习\早发白帝城1.txt'
y=open(filepath,encoding='utf-8')
content=y.read()

text=content.split('\n')
for i in text:
    print(i)


