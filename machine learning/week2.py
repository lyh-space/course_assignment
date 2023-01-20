# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 16:46
# @Author  : 李宇豪
# @File    : week2.py on PyCharm
# @Licence : CC BY-NC-SA


import numpy as np
a = np.random.randint(0, 21, (2, 6))
a = np.sqrt(a)
print("平方根后的a矩阵为：\n",a)

print("a矩阵的形状是", a.shape)
print("a矩阵数据的类型是", a.dtype)
print("a矩阵的最大元素是", a.max())
print("a矩阵的最小元素是", a.min())
print("a矩阵元素的平均值是", a.mean())

a = a.reshape(3, 4)
b = a - 3
b[b > 0] = 1
b[b != 1] = 0

print(b)
print("a矩阵中大于3的元素个数为",b.sum())


import matplotlib.pyplot as plt

x = np.linspace(0.01,5,1000)
y1=np.log(x)
y2=np.log(5*x)

p1,=plt.plot(x,y1,color="purple",linewidth=2.0,linestyle="-")
p2,=plt.plot(x,y2,color="green",linewidth=2.0,linestyle="-")

plt.xticks(np.arange(0, 6))
plt.yticks([-4,-2,0,2,4,6])

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', -0.2))

legend=plt.legend([p1,p2],["log(x)","log(5x)"],fontsize=12,loc='upper left')

plt.plot([3,3,3],[0,np.log(3),np.log(15)],linewidth=1.5,linestyle="--")
plt.scatter([3,3],[np.log(3),np.log(15)],50)

plt.show()
