import numpy as np
from machine_learning.supervised import Supervised


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1.0 - sigmoid(x))

class Perceptron(Supervised):

    def __init__(self, n_inputs, max_iter = 100000):
        np.random.seed(1)
        self.max_iter = max_iter
        self.w = 2 * np.random.random((n_inputs, 1)) - 1

    def format(self, data):
        return 1 if data > 0.5 else 0

    def fit(self, x, y):
        x = np.array(x)
        y = np.array(y).T
        for i in range(self.max_iter):

            out = self.predict(x)
            error = y - out

            adjust = np.dot(x.T, error * sigmoid_derivative(out))
            self.w += adjust

    def predict(self, x):
        x = np.array(x)
        x = x.astype(float)  
        return sigmoid(np.dot(x, self.w))
