'''
Softmax is a math formula that turns a list of numbers into probability.
And these probability:

Are always positive.

Always add up to 1.

We use it when a computer has to choose one option out of many — like whether a photo is of a cat, dog, or lion.
'''

import numpy as np 

# Softmax function
def softmax(x):
    # Subtract max value for numerical stability
    e_x = np.exp(x-np.max(x))

    # Softmax(xᵢ) = e^(xᵢ)/(e^(x₁)+e^(x₂)+e^(x₃)+...+e^(xₙ))
    return e_x/e_x.sum()
scores = np.array([3.0,1.0,0.2])
softmax_values = softmax(scores)

print("Scores: ",scores)
print("Softmax Values: ",softmax_values)