import numpy as np
from machine_learning.activates import sigmoid, sigmoid_derivative


class NeuralNetwork():
    def __init__(self, n_inputs):
        # np.random.seed(1)

        self.weights = 2 * np.random.random((n_inputs, 1)) - 1
        self.bias = 2 * np.random.random((n_inputs, 1)) - 1
        self.limit_iterations = 30000

    def predict(self, inputs):

        inputs = inputs.astype(float)
        return sigmoid(np.dot(inputs, self.weights + self.bias))

    def fit(self, inputs, outputs):

        for i in range(self.limit_iterations):
            y = self.predict(inputs)

            error = outputs - y

            adsust = np.dot(
                inputs.T,
                (2 * error) * sigmoid_derivative(outputs)
            )

            self.weights += adsust
            self.bias += adsust


