# Description: This is a sample file to demonstrate the usage of the Linear Regression model
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate some data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 3, 4, 5, 6])

# Fit a linear regression model
model = LinearRegression()
model.fit(x, y)

# Predict the values
predictions = model.predict(x)
print(predictions)

# Visualize designs
plt.scatter(x, y, color='blue')
plt.plot(x, predictions, color='red')
plt.show()