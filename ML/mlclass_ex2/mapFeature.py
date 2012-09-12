from numpy import *

def mapFeature(X1, X2):
    # MAPFEATURE Feature mapping function to polynomial features
    #
    #   MAPFEATURE(X1, X2) maps the two input features
    #   to quadratic features used in the regularization exercise.
    #
    #   Returns a new feature array with more features, comprising of
    #   X1, X2, X1**2, X2**2, X1*X2, X1*X2**2, etc..
    #
    #   Inputs X1, X2 must be the same size
    #

    degree = 6
    out = [ones(size(X1))]
    for i in range(1, degree+1):
        for j in range(i+1):
            out.append(X1 ** (i-j) * X2 ** j)

    if isscalar(X1):
        return hstack(out)  # if inputs are scalars, return a vector
    else:
        return column_stack(out)
