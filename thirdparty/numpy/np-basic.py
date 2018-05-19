#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np


'''
NumPy 是 Python 科学计算的基础包，它专为进行严格的数字处理而产生。
ndarray 是一个多维的数组对象，具有矢量算术运算能力和复杂的广播能力，并具有执行速度快和节省空间的特点。
ndarray 的一个特点是同构：即其中所有元素的类型必须相同。

ndarray 的常用属性
shape    - 各纬度大小
ndim     - 纬度个数
dtype    - 数据类型
itemsize - 每个元素占用内存空间大小，单位为字节
size     - 元素个数

ndarray 的常见创建方式
array()  - 通过列表和字典等来创建矩阵
zeros()  - 全0矩阵
ones()   - 全1矩阵
empty()  - 空矩阵 (实际有值，但其值是不确定的)
eyes()   - 单位矩阵
arange() - 序列矩阵
linspace() - 等差数列
logspace() - 等比数列，以10为底
fromstring() - 将字符串转换成ndarray对象
fromfunction() - 根据回调传回的矩阵行号和列号的参数生成矩阵的元素
tile()         - 重复元素
reshape()函数 - 改变矩阵形状，如从一维修改为二维；通过reshape生成的新数组和原始数组公用一个内存
通过元组可以指定创建的矩阵纬度
(3, 4) - 表示创建3*4的矩阵

ndarray 的数据类型
通过dtype属性来指定元素的数据类型
通过ndarray的astype()方法进行强制类型转换

ndarray 的四则运算
ndarray数组的四则运算是对数组里面的每个元素依次执行四则运算

Numpy常见数学函数
exp()  - 指数函数，底为e
exp2() - 指数函数，底为2
log()  - 对数函数，底为10
sqrt() - 平方根
sin()  - 正弦
cos()  - 余弦
tan()  - 正切
arcsin() - 反正弦
arccos() - 反余弦
arctan() - 反正切

ndarray常见数学函数
sum() - 求和
min() - 最小值
max() - 最大值
'''

lst = [1, 2, 3, 4, 5, 6]
arr = np.array(lst)     # 创建一维的ndarry对象
print(arr)              # [1 2 3 4 5 6]
print(type(arr))        # <class 'numpy.ndarray'>

lst2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
arr2 = np.array(lst2)   # 创建二维的ndarray对象
print(arr2)
print(arr2.shape)       # (2, 5) - 即2行5列
print(arr2.ndim)        # 2      - 2个纬度
print(arr2.dtype)       # int32  - 元素数据类型为32位整型
print(arr2.itemsize)    # 4      - 每个元素占用内存空间大小为4个字节
print(arr2.size)        # 10     - 数组总共有10个元素

arr_zeros = np.zeros(5)
print(arr_zeros)         # [0. 0. 0. 0. 0.]

arr_ones = np.ones(5)
print(arr_ones)         # [1. 1. 1. 1. 1.]

arr_empty = np.empty(5)
print(arr_empty)        # [1. 1. 1. 1. 1.]
arr_empty2 = np.empty((3, 4))   # 创建3*4的空矩阵

arr_eye = np.eye(3)     # 创建3阶单位矩阵
print(arr_eye)

arr_range = np.arange(5)
print(arr_range)        # [0 1 2 3 4]

arr_reshape = arr.reshape((2, 3))   # 将一维矩阵更改为2*3矩阵
print(arr_reshape)
'''
[[1 2 3]
 [4 5 6]]
'''
print(np.arange(9).reshape((3, 3)))     # 生成3*3的序列矩阵
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''

# 新数组的shape属性应该要与原来数组的一致，即新数组元素数量与原数组元素数量要相等。
# 一个参数为-1时，那么reshape函数会根据另一个参数的维度计算出数组的另外一个shape属性值。
print(np.arange(8).reshape((2, -1)))    # -1表示根据其他已知维度 (行为2)，自动计算当前-1所在的实际维度 (计算出列为4)


# 等差数列
arr_lin = np.linspace(1, 9, 5)
print(arr_lin)          # [1. 3. 5. 7. 9.]

# 等比数列
arr_log = np.logspace(0, 3, 4)  # 以10为底的指数函数
print(arr_log)                  # [   1.   10.  100. 1000.]
print(type(arr_log))            # <class 'numpy.ndarray'>

# 将字符串转换成ndarray对象
str_ascii = "abcdefg"
a = np.fromstring(str_ascii, dtype=np.int8)
print(a)                        # [ 97  98  99 100 101 102 103]


# 根据回调函数生成矩阵元素
def func(i, j):
    return i+j


a = np.fromfunction(func, (2, 3))
print(a)
'''
[[0. 1. 2.]
 [1. 2. 3.]]
'''

a = np.arange(1, 5).reshape((2, -1))
print(np.tile(a, (2, 3)))       # 2表示行上重复2次，3表示列上重复3次
'''
[[1 2 1 2 1 2]
 [3 4 3 4 3 4]
 [1 2 1 2 1 2]
 [3 4 3 4 3 4]]
'''


# 指定创建浮点类型的数组
arr_float = np.array(lst, dtype=np.float)
print(arr_float)        # [1. 2. 3. 4. 5.]
print(arr_float.dtype)  # float64

# 将浮点类型转换成整型
arr_int = arr_float.astype(np.int64)
print(arr_int)          # [1 2 3 4 5]
print(arr_int.dtype)    # int64


# 矩阵的运算
# 1. 矩阵的线性运算
# A+B  矩阵对应元素相加
# A-B  矩阵对应元素相减
# A*B  矩阵对应元素相乘
# A/B  矩阵对应元素相除
# A%B  矩阵对应元素取模
# A**n 矩阵对应元素n次方
# kA   矩阵对应元素与k相乘，数乘运算
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
print(a + b)        # [11 22 33 44]
print(a - b)        # [ 9 18 27 36]
print(a * b)        # [ 10  40  90 160]
print(a / b)        # [10. 10. 10. 10.]
print(a ** 2)       # [ 100  400  900 1600]
print(a * 2)        # [20 40 60 80]

# 2. 矩阵的乘法 (C = AB)
# 只有当左边矩阵的列数等于右边矩阵的行数时，两个矩阵才能进行乘法运算
a = np.array([[2, 3], [1, -2], [3, 1]])
b = np.array([[1, -2, -3], [2, -1, 0]])
print(a.shape[1] == b.shape[0])     # True
print(a.dot(b))
'''
[[ 8 -7 -6]
 [-3  0 -3]
 [ 5 -7 -9]]
'''


# 矩阵的截取操作
# 1. 按行列截取
# a里面是包含两个子元素，每个子元素都是一个行向量，故在未指定行标时，是对a的子元素进行切片操作
a = np.arange(1, 11).reshape((2, 5))
print(a)
'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
'''
print(a[0:1])           # 截取第一行 [[1 2 3 4 5]]
print(a[1, 2:5])        # 截取第二行的[2, 5)列 [ 8  9 10]
print(a[1, :])          # 截取第二行，冒号表示直接复制行 [ 6  7  8  9 10]

print(a[[0, 1], [1, 1]])    # [2 7]

# 2. 按条件截取
print(a[a > 6])         # 截取矩阵a中值大于6的元素，返回一维数组 [ 7  8  9 10]

b = a > 6               # 生成布尔矩阵
print(b)
'''
[[False False False False False]
 [False  True  True  True  True]]
'''

a[a > 6] = 0            # 将矩阵中值大于6的元素全部赋值为0
print(a)
'''
[[1 2 3 4 5]
 [6 0 0 0 0]]
'''


# 矩阵的合并操作
# hstack() - 横向合并，列数增加
# vstack() - S纵向合并，行数增加
# concatenate((a, b), axis=0)    # 同vstack()
# concatenate((a, b), axis=1)    # 同hstack()
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.hstack((a, b)))
print(np.vstack((a, b)))
print(np.concatenate((a, b), axis=0))
print(np.concatenate((a, b), axis=1))

# 矩阵的分离操作
arrays = np.split(a, 2)    # [array([[1, 2]]), array([[3, 4]])]
print(arrays[0])           # [[1 2]]
print(arrays[1])           # [[3 4]]

# 矩阵的复制操作
b = np.copy(a)
print(b)
print(id(a))                # 1186206767824
print(id(b))                # 1186206767104


# 矩阵的转置
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.transpose())
print(a.T)


# 矩阵信息获取
# 1. 最大值与最小值
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.max())      # 6
print(a.min())      # 1

# 可以指定关键字参数axis来获得行最大（小）值或列最大（小）值
# axis=0 行方向最大（小）值，即获得每列的最大（小）值 (横坐标 x轴)
# axis=1 列方向最大（小）值，即获得每行的最大（小）值 (纵坐标 y轴)
print(a.max(axis=0))        # [4 5 6]
print(a.max(axis=1))        # [3 6]

# 获取最大值元素所在位置
print(a.argmax(axis=1))     # [2 2]
print(a.argmin(axis=1))     # [0 0]

# 2. 平均值
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.mean())             # 3.5
print(a.mean(axis=0))       # [2.5 3.5 4.5]
print(a.mean(axis=1))       # [2. 5.]

# 3. 方差
# 方差函数var()相当于函数mean(abs(x - x.mean())**2),其中x为矩阵
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.var())              # 2.9166666666666665
print(a.var(axis=0))        # [2.25 2.25 2.25]
print(a.var(axis=1))        # [0.66666667 0.66666667]

# 4. 标准差
# 标准差函数std()相当于sqrt(mean(abs(x - x.mean())**2))，或相当于sqrt(x.var())
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.std())              # 1.707825127659933
print(a.std(axis=0))        # [1.5 1.5 1.5]
print(a.std(axis=1))        # [0.81649658 0.81649658]

# 5. 中位数
# 中值指的是将序列按大小顺序排列后，排在中间的那个值，如果有偶数个数，则是排在中间两个数的平均值
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.median(a))             # 3.5
print(np.median(a, axis=0))     # [2.5 3.5 4.5]
print(np.median(a, axis=1))     # [2. 5.]

# 6. 求和
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.sum())                  # 21
print(a.sum(axis=0))            # [5 7 9]
print(a.sum(axis=1))            # [ 6 15]

# 7. 累积和
# 某位置累积和指的是该位置之前(包括该位置)所有元素的和
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.cumsum())               # [ 1  3  6 10 15 21]
print(a.cumsum(axis=0))
'''
[[1 2 3]
 [5 7 9]]
'''
print(a.cumsum(axis=1))
'''
[[ 1  3  6]
 [ 4  9 15]]
'''


# 广播
