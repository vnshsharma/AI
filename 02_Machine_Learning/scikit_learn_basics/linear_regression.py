# Linear Regression is a way to find the best straight line that goes through your data.

# This pattern is used to predict for 5 hours — even though 5 wasn’t in the training data.

'''
Example: It learns the pattern from the given data and then guesses(predicts) the value for new input.

| Study Hours | Marks |
| ----------- | ----- |
| 1           | 10    |
| 2           | 20    |
| 3           | 30    |

Marks = 10 X Hours
Marks = 10 X 4 = 40
'''

from sklearn.linear_model import LinearRegression
x = [[1], [2], [3]]
y = [10,20,30]

model = LinearRegression()
model.fit(x,y)

print(f'Predicted for 4:',model.predict([[4]]))