# It learns the pattern from the given dataand then guesses (predicts) the value for new input.

'''
It answers questions like:

Is it Yes or No?
Is it Spam or Not Spam?
Is the email important or not?

| Hours Studied | Pass (1) / Fail (0) |
| ------------- | ------------------- |
| 1             | 0                   |
| 2             | 0                   |
| 3             | 1                   |
| 4             | 1                   |
"If someone studies 2.5 hours, there’s a 60% chance they will pass."

OUTPUT: Gives a probability (like 0.8)
        You convert it to class:
        If prob > 0.5 → Class 1 (Pass)
        If prob < 0.5 → Class 0 (Fail)
'''


from sklearn.linear_model import LogisticRegression

x = [[0], [1], [2], [3]]
y = [0,0,1,1]

model = LogisticRegression()
model.fit(x,y)

print("Prediction for 2.5:",model.predict([[2.5]]))