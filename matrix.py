import math
import numpy as np
def f(x):
    y = 1/(1+np.exp(-x))
    #print(y)
    return y

def f_deriv(x):
    y = f(x)*(1-f(x))
    #print(y)
    return y

inputs = np.array([[1],[1],[0]])
weights = np.array([[1,4,6],[5,2,7],[3,9,8]])

learning_rate = 0.01
total = weights.dot(inputs)
print(total)

yy =[]

for x in total:
    for i in x:
        i = f(x)
        yy.append(i)

print(yy)

weights2 = np.array([0.6,0.6,0.75])
outputs = weights2.dot(yy)
outputs = outputs[0]

print(outputs)

final_res = f(outputs)

print(final_res)




