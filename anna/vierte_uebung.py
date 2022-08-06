import matplotlib.pyplot as plt
import math
import random

# number_of_loops
n = 1000000

# pi
pi = 3.14159265359

x=[]
y=[]

def zahl(i):
    return i/10000

def rauschen():
   sigma = 0.5
   return random.normalvariate(0,sigma)

for i in range(n):
    x.append(zahl(i) * math.cos(zahl(i)) + rauschen())
    y.append(zahl(i) * math.sin(zahl(i)) + rauschen())


plt.figure(figsize=(15, 15))
plt.plot(x,y)
plt.show()
