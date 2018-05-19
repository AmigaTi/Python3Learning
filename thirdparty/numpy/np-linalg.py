#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
# from numpy import linalg

'''
linalg - linear algebra - 线性代数

numpy.linalg中的常用函数
diag    以一维数组的形式返回方阵的对角线元素 (n阶对角矩阵)
dot     矩阵乘法
trace   计算对角线元素的和
det     计算矩阵行列式
eig     计算方阵的本征值和本征向量
inv     计算方阵的逆
pinv    计算矩阵的Moore-Penrose伪逆
qr      计算qr分解
svd     计算奇异值分解
solve   解线性方程组Ax=b，其中A为一个方阵
lstsq   计算Ax=b的最小二乘解
transpose  矩阵的转置
norm    n维向量的范数(长度)
'''

# 求解二元线性方程组 - 二阶行列式计算
# 2x1 + 3x2 = 8
# x1 - 2x2 = -3
d_a = np.array([[2, 3], [1, -2]])       # 系数行列式 - 由方程组的系数所确定
d_b = np.array([[8], [-3]])             #
print(np.linalg.solve(d_a, d_b))        # x1 = 1, x2 = 2
'''
[[1.]
 [2.]]
'''


# 逆矩阵 (p53-例3)
a = np.array([[1, 0, 1], [2, 1, 0], [-3, 2, -5]])
print(np.linalg.inv(a))
'''
[[-2.5  1.  -0.5]
 [ 5.  -1.   1. ]
 [ 3.5 -1.   0.5]]
'''
