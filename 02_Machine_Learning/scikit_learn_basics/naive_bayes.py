'''
Naive Bayes assumes that features are independent, and uses probability to guess the most likely class.

EXAMPLE: 
        To classify a message as spam or not spam, it calculates:

            How often certain words appear in spam vs. non-spam

            Then uses probability to predict the category
'''


from sklearn.naive_bayes import GaussianNB

x = [[1], [2], [3], [4]]
y = [0,0,1,1]

model = GaussianNB()
model.fit(x,y)

print('Prediction for 2.5:',model.predict([[2.5]]))