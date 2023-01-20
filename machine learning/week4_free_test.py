# -*- coding: utf-8 -*-
# @Time    : 2022/9/20 9:01
# @Author  : 李宇豪
# @File    : week4_free_test.py on PyCharm
# @Licence : CC BY-NC-SA

import numpy as np
from sklearn.linear_model import SGDRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from matplotlib import pyplot as plt

# 划分数据集
data_boston = load_boston()
X_train, X_test, Y_train, Y_test = train_test_split(data_boston.data, data_boston.target)

# 特征缩放
X_scaler = StandardScaler()
Y_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
Y_train = np.ravel(Y_scaler.fit_transform(Y_train.reshape(-1, 1)))
X_test = X_scaler.transform(X_test)
Y_test = np.ravel(Y_scaler.transform(Y_test.reshape(-1, 1)))

xx = np.linspace(-3, 3, 100)
yy = xx

model = SGDRegressor(eta0=0.01)
scores = cross_val_score(model, data_boston.data, data_boston.target,scoring='r2', cv=5)
print("交叉验证R方评分为：%s" % scores)
print("交叉验证R方评分的平均值为：%s" % np.mean(scores))
model.fit(X_train, Y_train)
print("模型参数为：", model.coef_)
print("测试集的R方评分为：%s" % model.score(X_test, Y_test))
print("————————————————————")
plt.scatter(model.predict(X_train), Y_train, c="blue")
plt.scatter(model.predict(X_test), Y_test, c="red")
plt.plot(xx, yy, c='black', linewidth=1.5)
plt.show()


