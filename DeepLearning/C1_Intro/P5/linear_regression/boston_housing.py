import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

# 且看后续发展如何预处理二维数据

data = pd.read_csv("./data/housing.csv")
print(data.head())

# 为了更轻松地训练网络，我们将对每个连续变量标准化，即转换和调整变量，使它们的均值为 0，标准差为 1。
quant_features = {'RM', 'LSTAT', 'PTRATIO', 'MEDV'}
scaled_features = {}
for each in quant_features:
    mean, std = data[each].mean(), data[each].std()
    scaled_features[each] = [mean, std]
    data.loc[:, each] = (data[each] - mean)/std

# 划分x, y
target_fields = ['MEDV']

features, targets = data.drop(target_fields, axis=1), data[target_fields]
x = features
y = targets
print(x.head())
print(y.head())

# model
model = linear_model.LinearRegression()
model.fit(x, y)

# test data
sample_house = [[2.29690000e-01, 0.00000000e+00, 1.05900000e+01, 0.00000000e+00, 4.89000000e-01,
                6.32600000e+00, 5.25000000e+01, 4.35490000e+00, 4.00000000e+00, 2.77000000e+02,
                1.86000000e+01, 3.94870000e+02, 1.09700000e+01]]

# predict
model.predict(sample_house)










