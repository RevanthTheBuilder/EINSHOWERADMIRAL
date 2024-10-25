
# Project: Machine Learning Model for Predictive Analytics
# Language: Python
# Libraries: Scikit-learn, Pandas, NumPy, Matplotlib

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data
data = {'Size': [1500, 2500, 3500, 4500, 5500],
        'Price': [300000, 400000, 500000, 600000, 700000]}
df = pd.DataFrame(data)

# Prepare data
X = df[['Size']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Plot results
plt.scatter(X_test, y_test, color='red')
plt.plot(X_test, predictions, color='blue')
plt.title('Predicted Prices')
plt.xlabel('Size')
plt.ylabel('Price')
plt.savefig('predicted_prices.png')
plt.close()
