# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 17:06
# @Author  : 李宇豪
# @File    : week1.py on PyCharm
# @Licence : CC BY-NC-SA

'''
2022fall 数值计算 李华山
week1 上机练习
'''

'''
第一题：
请编写一个python程序，找出[1500, 1550]区域的质数。(注意：range函数取值范围不包括上限。)
'''
print("第一题：")

for j in range(1500, 1551):
    for k in range(2, j):
        if j%k == 0:
            break
    else:
        print(j, "是素数")

print("--------------------")

'''
第二题：
阶乘的定义是  f(0)=1, f(n)=f(n-1)*n, 请编写函数用于计算f(i)的值，其中i为任意非负整数，引用函数并输出f(9)的值。
'''
print("第二题：")

def fun(n):
    if (not isinstance(n,int)) or (n < 0):
        print("输入错误")
    else:
        if n == 0:
            return 1
        else:
            return fun(n - 1) * n
print("9!=", fun(9))

print("--------------------")

'''
第三题：
冒泡排序：是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
请写一个运用冒泡排序法进行排序的函数，然后随机生成包含10个100以内整数的数组，并调用函数进行排序，输出原来的和排序后的数组。
'''
print("第三题：")

import numpy as np
a = np.random.randint(1,100,10)
print("排序前数组为：", a)
n = len(a)
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print("排序后数组为：", a)