import numpy as np
from decimal import Decimal
from machine_learning.activates import sigmoid, sigmoid_derivative


class Perceptron():

    def __init__(self, n_inputs, max_iter = 100000):
        # np.random.seed(1)
        self.max_iter = max_iter
        self.b = np.random.rand()
        self.w = 2 * np.random.random((n_inputs, 1)) - 1
        self.rate = np.random.rand()

    def fit(self, x, y):
        x = np.array(x, dtype=float)
        y = np.array(y, dtype=float).T
        for i in range(self.max_iter):

            out = self.predict(x)
            error = y - out

            adjust = np.dot(x.T, error * sigmoid_derivative(out)) * self.rate
            self.w += adjust
            self.b += adjust

    def predict(self, x):
        x = np.array(x, dtype=float)
        x = np.dot(x, self.w)
        return sigmoid(x)
