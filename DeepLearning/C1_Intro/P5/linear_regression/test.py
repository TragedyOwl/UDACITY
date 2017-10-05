import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_fwf('./data/challenge_dataset.txt')
# print(dataframe)

x_values = dataframe['data'].str.split(',', expand=True)[0]
y_values = dataframe['data'].str.split(',', expand=True)[1]
# print(x_values)

df = pd.DataFrame()
df['x'] = x_values
df['y'] = y_values
# print(df)

x_values = df[['x']]
y_values = df[['y']]

#train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

#visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()







