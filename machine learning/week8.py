# -*- coding: utf-8 -*-
# @Time    : 2022/11/4 9:21
# @Author  : 李宇豪
# @File    : week8.py on PyCharm
# @Licence : CC BY-NC-SA

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate


def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy


def plot_contour(clf, xx, yy, X_train, y_train, **kwargs):
    clf.fit(X_train, y_train)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = plt.contourf(xx, yy, Z, **kwargs)
    return out


iris = datasets.load_iris()
X = iris.data[:, 1:3]
y = iris.target
X0, X1 = X[:, 0], X[:, 1]
xx, yy = make_meshgrid(X0, X1)
model = SVC(kernel='rbf')

# 网格搜索
param_grid = {'gamma': np.arange(0.0395, 0.0405, 0.001),
              'C': np.arange(0.605, 0.615, 0.001)}
# [0.001,0.01,0.1,1,10]}
clf = GridSearchCV(model, param_grid, cv=5)
clf.fit(X, y)
best_parameters = clf.best_params_
print("网格搜索结果：")
print('grid search best param:\n {0}'.format(best_parameters))
print('grid search best score:{0:.3f}\n'.format(clf.best_score_))

# 画图
models = (SVC(kernel='rbf', gamma=0.0405, C=0.611),
          SVC(kernel='rbf', gamma=0.01, C=0.611),
          SVC(kernel='rbf', gamma=10, C=0.611))
titles = ('SVC with RBF kernel : gamma=0.0405 ',
          'SVC with RBF kernel : gamma=0.01 ',
          'SVC with RBF kernel : gamma=10 ')

for clf, title in zip(models, titles):
    cv_result = cross_validate(clf, X, y, cv=5)
    cv_value_vec = cv_result["test_score"]
    cv_mean = np.mean(cv_value_vec)
    print(title, "score:", '%.3f' % cv_mean)
    plot_contour(clf, xx, yy, X, y, cmap=plt.cm.coolwarm, alpha=0.8)

    plt.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='black')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xlabel('Sepel length')
    plt.ylabel('Sepel width')
    plt.xticks(())
    plt.yticks(())
    plt.title(title)
    plt.show()
    plt.clf()
