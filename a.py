## not working linear regresion algorithm


from cmath import cos
import numpy as np
import math
from pyparsing import delimited_list
def cost_fun(x, y, theta):
    predictions = theta[1]*x + theta[0]
    sqr_error = (predictions - y) ** 2
    J = (1 / (x.size)) * sum(sqr_error)
    return J 

def gradient_descent(X, Y):
    # Building the model
    X = np.array(X)
    Y = np.array(Y)
    
    m = 0
    c = 0

    L = 0.01  # The learning Rate
    epochs = 1000  # The number of iterations to perform gradient descent

    n = X.size # Number of elements in X
    # Performing Gradient Descent 
    for i in range(epochs):
        Y_pred = m*X + c  # The current predicted value of Y
        D_m = (-1/n) * sum((Y - Y_pred) * X)  # Derivative wrt m
        D_c = (-1/n) * sum(Y - Y_pred)  # Derivative wrt c
        m = m - L * D_m  # Update m
        c = c - L * D_c  # Update c
        
    print(cost_fun(X,Y,[m,c]))
    print(m, c)
    

#print(gradient_descent([[1,1],[1,2],[1,3]],[1,2,3]))
data = np.loadtxt('/home/pills/Downloads/ML Lecture Slides Coursera/Week 2 excercise/ex1data1.txt', delimiter=',')
x = data[0]
y = data[1]
print(gradient_descent(x,y))