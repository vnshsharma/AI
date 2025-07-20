'''
SVM draws a boundary line that best separates the classes, and tries to keep it as far as possible from all points.

If you have two types of animals (cats and dogs), SVM finds the best wall between them so it can classify any new animal.
'''


from sklearn.svm import SVC

x = [[1], [2], [3], [4]]
y = [0,0,1,1]

model = SVC()
model.fit(x,y)

print("SVM prediction for 3:",model.predict([[3]])) 