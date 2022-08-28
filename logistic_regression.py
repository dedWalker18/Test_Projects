# this is just a simple logistic regression model and it probably wont be very accurate for most of the cases

from audioop import bias
import numpy as np

class LogisticRegression:
    
    def __init__(self, lr=0.01, num_iters=1000):
        self.lr = lr
        self.num_iters = num_iters
        self.weights =  None
        self.bias = None
        
    def fit(self, X, y):
        # init parameters
        num_samples, num_features = X.shape
        self.weights = np.zeros(num_features)
        self.bias = 0
        
        # gradient descent
        for _ in range(self.num_iters):
            linear_model = np.dot(X, self.weights) + self.bias
            y_predicted = self.sigmoid(linear_model)        
            
            # update weights 
            dw = (1 / num_samples) * np.dot(X.T, (y_predicted  - y))
            db = (1 / num_samples) * np.sum(y_predicted  - y)
            
            self.weights -= self.lr * dw
            self.bias -= self.bias * db
            
            
    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self.sigmoid(linear_model)
        prediction = [1 if i > 0.5 else 0 for i in y_predicted]
        return prediction    

    def sigmoid(Self, x):
        return 1 / (1 + np.exp(-x))
    