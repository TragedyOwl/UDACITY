import numpy as np

s = np.array(5)     #标量
x = s + 3

v = np.array([1, 2, 3])     # 向量

# https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html
# 高级访问方式--切片语法
# print(v[1:])

m = np.array([[1,2,3], [4,5,6], [7,8,9]])   # 矩阵
# print(m.shape)

t = np.array([[[[1],[2]],[[3],[4]],[[5],[6]]],[[[7],[8]],[[9],[10]],[[11],[12]]],[[[13],[14]],[[15],[16]],[[17],[17]]]])    # 张量
# print(t[2][1][1][0])

v = np.array([1,2,3,4])
x = v.reshape(1, 4)     # 1*4
# print(x)

# 1*4
x = v[None, :]
# print(x)

# 4*1
x = v[:, None]
# print(x)


print(233)


