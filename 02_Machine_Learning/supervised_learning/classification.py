from sklearn.linear_model import LogisticRegression

x = [[0], [1], [2], [3]]
y = [0,0,1,1]

model = LogisticRegression()
model.fit(x,y)

print('Prediction for 2.5:',model.predict([[2.5]])) 