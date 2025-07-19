# regression.py
# 📘 Linear Regression Example using scikit-learn (Supervised Learning)

from sklearn.linear_model import LinearRegression

# Sample training data (input features and target values)
X = [[1], [2], [3], [4]]   # Example: Study hours
y = [10, 20, 30, 40]       # Example: Marks scored

# Create the Linear Regression model
model = LinearRegression()

# Train (fit) the model with the data
model.fit(X, y)

# Make a prediction for 5 hours of study
prediction = model.predict([[5]])

print("Predicted marks for 5 hours of study:", prediction)