import numpy as np
from abc import ABC, abstractmethod

class Layer(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.inputs = None
        self.output = None
        self.dinputs = None

    @abstractmethod
    def forward(self):
        pass

    @abstractmethod
    def backward(self):
        pass

class Layer_Dense(Layer):
    # Layer initialization
    def __init__(self, n_inputs, n_neurons,
                weight_regularizer_l1=0, weight_regularizer_l2=0,
                bias_regularizer_l1=0, bias_regularizer_l2=0) -> None:
        super().__init__()
        # Initialize weights and biases
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons) 
        self.biases = np.zeros((1, n_neurons))
        # Set regularization strength
        self.weight_regularizer_l1 = weight_regularizer_l1
        self.weight_regularizer_l2 = weight_regularizer_l2
        self.bias_regularizer_l1 = bias_regularizer_l1
        self.bias_regularizer_l2 = bias_regularizer_l2
         
    # Forward pass
    def forward(self, inputs):

        # storing inputs to compute partial derivative later on 
        self.inputs = inputs

        # Calculate output values from inputs, weights and biases
        self.output = np.dot(inputs, self.weights) + self.biases

    # Backward pass
    def backward(self, dvalues):

        # Gradients on parameters
        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims= True) 

        # Gradient on values
        self.dinputs = np.dot(dvalues, self.weights.T)

"""
class Dropout(object):
    pass
"""