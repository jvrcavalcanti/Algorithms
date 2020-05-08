import numpy as np


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))
    ''' Não estoura '''
    # if inx>=0:      
    #     return 1.0/(1+exp(-inx))
    # else:
    #     return exp(inx)/(1+exp(inx))


def sigmoid_derivative(x):
    return sigmoid(x) * (1.0 - sigmoid(x))

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return 1. * (x > 0)
