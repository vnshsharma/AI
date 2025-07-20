'''
If you want to know whether a new student likes Math or Science, look at their K nearest classmates.
If most of them like Math, assume this one does too.
'''



from sklearn.neighbors import KNeighborsRegressor

# Training data
X = [[1], [2], [3], [4]]
y = [10, 20, 30, 40]

# Create and train the model
model = KNeighborsRegressor(n_neighbors=2)
model.fit(X, y)

# Predict for 2.5
print('KNN Prediction for 2.5:', model.predict([[2.5]]))
