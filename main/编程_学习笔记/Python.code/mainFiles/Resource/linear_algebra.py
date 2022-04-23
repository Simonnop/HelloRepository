from cmath import sqrt

def dot(vector1,vector2):
    sum=0
    for i,j in zip(vector1,vector2):
        sum+=i*j
    return sum

def add(vector1,vector2):
    newVector=[]
    for i,j in zip(vector1,vector2):
        newVector.append(i+j)
    return newVector

def subtract(vector1,vector2):
    newVector=[]
    for i,j in zip(vector1,vector2):
        newVector.append(i-j)
    return newVector

def scalar_multiply(num,vector1):
    newVector=[]
    for i in vector1:
        newVector.append(i*num)
    return newVector

def distance(vector1,vector2):
    distSqr=0
    for i,j in zip(vector1,vector2):
        distSqr+=(i-j)**2
    return sqrt(distSqr)



