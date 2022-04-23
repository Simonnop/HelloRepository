import random
import matplotlib.pyplot as plt

def GapFunc(data,para):
    slope,intercept=para
    return sum([(x*slope+intercept-y)**2 for x,y in data])/len(data)

def Scalar_multiply(num,vector1):
    newVector=[]
    for i in vector1:
        newVector.append(i*num)
    return newVector

def Add(vector1,vector2):
    newVector=[]
    for i,j in zip(vector1,vector2):
        newVector.append(i+j)
    return newVector    

def PianFen(func,vectors,i,h,data):
    vectors_temp=[]
    for j,vector_j in enumerate(vectors):
        vectors_temp.append(0)
        if j==i:
            vectors_temp[j]=vector_j+h
        else:
            vectors_temp[j]=vector_j
    return (func(data,vectors_temp)-func(data,vectors))/h

def Gradient(func,vectors,h,data):
    return [PianFen(func,vectors,i,h,data) for i in range (len(vectors))]

def Gradient_step(vectors,step_size,func,h,data):
    step=Scalar_multiply(step_size,Gradient(func,vectors,h,data))
    return Add(vectors,step)

friends=[70,65,72,63,71,64,60,64,67]
minutes=[175,170,205,120,220,130,105,145,190]
data=list(zip(friends,minutes))

para=[random.uniform(-100,100) for _ in range(2)]
h=0.000001
step_size=-0.0001
times=10000000

for epoch in range(times+1):
    para=Gradient_step(para,step_size,GapFunc,h,data)
    if epoch%500000==0:
        m,b=para
        print(
            '---------------------------------------------------------\n',
            'Iteration:',epoch,'\n',
            'm=',m,',b=',b,',grad=',Gradient(GapFunc,para,h,data),'Error=',GapFunc(data,para),
            '\n'
        )

m,b=para
lineDot_x=[x for x in range(100)]
lineDot_y=[x*m+b for x in range(100)]
plt.plot(lineDot_x,lineDot_y,linestyle=':',color='r')
plt.scatter(friends,minutes)
plt.axis([54,75,50,250])
plt.xlabel('numbers of friends')
plt.ylabel('minutes online')
plt.show()




