import matplotlib.pyplot as plt
import random
import math

guassList=[random.gauss(70,5) for _ in range(1000)]
plt.hist(guassList,bins=20,density=True)
plt.show()

numList=[x/100 for x in range(5000,9001)]
# 这个错了,但看不出在哪  funcList=[(1/((math.sqrt(2*3.1415))*5))*((2.7182)**-((x-70)**2)/(2*(5**2))) for x in numList]
funcList=[(2.7182**((-(x-70)**2)/50))/((math.sqrt(2*3.1415))*5) for x in numList]
plt.hist(guassList,bins=20,density=True)
plt.plot(numList,funcList)
plt.show()

