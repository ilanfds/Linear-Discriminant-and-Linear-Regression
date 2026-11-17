import numpy as np


def leastSquares(data, label):
    # Sum of squared error shoud be minimized
    #
    # INPUT:
    # data        : Training inputs  (num_samples x dim)
    # label       : Training targets (num_samples x 1)
    #
    # OUTPUT:
    # weights     : weights   (dim x 1)
    # bias        : bias term (scalar)

    #####Insert your code here for subtask 1a#####
    # Extend each datapoint x as [1, x]
    # (Trick to avoid modeling the bias term explicitly)
    num_samples = data.shape[0]

    # Prepend a column of ones: X = [1, x]
    data_extended = np.hstack((np.ones((num_samples, 1)), data))

    # Normal equation: w = (X^T X)^-1 X^T y
    w = np.linalg.inv(data_extended.T @ data_extended) @ data_extended.T @ label

    bias = w[0]
    weight = w[1:]

    return weight, bias
