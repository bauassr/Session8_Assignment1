# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 19:42:45 2018

@author: singh.shivam
"""
import numpy as np 
import matplotlib.pyplot as plt
l  = [i  for i in range(1,13)]
x = np.array(l)
print(x)

maxy=np.array([39,41,43,47,49,51,45,38,37,29,27,25])
miny=np.array([21,23,27,28,32,35,31,28,21,19,17,18])
#calculate polynomial
Z=np.polyfit(x,maxy,6)
V = np.polyfit(x,miny,6)
print(Z)
f=np.poly1d(Z)
f1=np.poly1d(V)

#caculate new x, y 
x_new=np.linspace(x[0],x[-1],12)
y_new=f(x_new)
x1_new=np.linspace(x[0],x[-1],12)
y1_new=f1(x1_new)

plt.plot(x,maxy,'o',x_new,y_new,"blue")
plt.plot(x,miny,'o',x1_new,y1_new,"orange")
plt.xlim()
plt.ylabel('Temperature (degree C)')
plt.xlabel('Months')
plt.show() 