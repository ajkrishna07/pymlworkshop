import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as plot
from sklearn.datasets import load_breast_cancer
#%matplotlib inline

cancer = load_breast_cancer()
features = pd.DataFrame(cancer.data,columns=cancer.feature_names)
target = pd.DataFrame(cancer.target,columns=['TARGET'])
data = pd.concat([features,target], axis=1)
a = data.corr('pearson')
x = np.array(data['worst concave points'])
y = np.array(data['TARGET'])

x = x/x.mean()
plt.plot(x,y,'r.')
plt.show()

div = int(0.8 * len(x))

x_train = x[:div]
y_train = y[:div]

x_test = x[div:]
y_test = y[div:]

def sigmoid(x):
    return 1/(1+np.exp(-x))
	
def sqerror(a,b,x,y):
    error = 0
    N = len(x)
    for i in range(N):
        f = (a*x[i])+b
        error += (y[i]-sigmoid(f))**2
    return (1/N) * error
	
def step_gradient(a,b,x,y,learning_rate):
    grad_a = 0
    grad_b = 0
    m = len(x)
    for i in range(m):
        f = (a*x[i])+b
        grad_a += (sigmoid(f)-y[i])*x[i]
        grad_b += (sigmoid(f)-y[i])
    
    a = a-(grad_a*learning_rate)
    b = b-(grad_b*learning_rate)
    return a,b

def descend(initial_a,initial_b,x,y,learning_rate,iterations):
    a,b = initial_a,initial_b
    for i in range(iterations):
        if i % 1000 == 0:
            e = sqerror(a,b,x,y)
            print("Error: %.5f, a: %.5f, b: %.5f"%(e,a,b))
        a,b = step_gradient(a,b,x,y,learning_rate)
    return a,b
	
a,b = -6.84903,7.72128
learning_rate = 0.001
iterations = 10000

final_a,final_b = descend(a,b,x_train,y_train,learning_rate,iterations)

plt.plot(x_train,y_train,'r.',x_train,sigmoid(final_a*x_train+final_b),'bo')
plt.show()