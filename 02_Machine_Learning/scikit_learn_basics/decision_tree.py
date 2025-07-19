# A Decision Tree is a model that makes decisions like a flowchart
# It asks yes/no questions at each step, and based on the answer, it goes down a branch.

'''
EXAMPLE: 

| Attendance (%) | Study Hours | Result |
| -------------- | ----------- | ------ |
| 80             | 2           | Pass   |
| 60             | 1           | Fail   |
| 90             | 3           | Pass   |
| 50             | 0           | Fail   |

If Attendance > 70:
   → Pass
Else:
   → Fail


'''

from sklearn.tree import DecisionTreeClassifier

x = [[80], [60], [90], [50]]
y = ['Pass','Fail','Pass','Fail']

model = DecisionTreeClassifier()
model.fit(x,y)

print(f'Prediction for 70:', model.predict([[70]]))