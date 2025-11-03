from sklearn.linear_model import LinearRegression  
import numpy as np


x = np.array([2,4,6,8,10]).reshape(-1,1)
y = np.array([20,40,60,80,100])
model = LinearRegression()

model.fit(x,y)
pred = model.predict([[290]])
print("Predicted marks : " , pred[0])