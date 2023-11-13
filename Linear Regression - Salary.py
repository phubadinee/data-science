import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("D:\Mahagraph Coding\มหากาพย์โค้ดดิ้ง Python\Machine Learning\Salary_Data.csv")

x = dataset['YearsExperience'].array
y = dataset['Salary'].array

plt.grid()
plt.scatter(x,y, color='r')
plt.title("Salary")
plt.show()

from sklearn.linear_model import LinearRegression
x  = x.reshape(-1,1)
y  = y.reshape(-1,1)

model = LinearRegression()
model.fit(x,y)

prd = model.predict(x)

plt.grid()
plt.scatter(x,y,color='r')
plt.plot(x,prd,linewidth='3')
plt.title("Salary Linear Regression")

print('m = ',model.coef_[0][0],'\nb = ',model.intercept_[0])

x_predict = [[25]]
predict = model.predict(x_predict)
print(f'{x_predict[0][0]} is {predict[0][0]}')
