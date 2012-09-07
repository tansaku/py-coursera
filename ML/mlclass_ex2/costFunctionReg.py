from mlclass_ex2 import *
from numpy import *

def costFunctionReg(theta, X, y, lambda_):
    #COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
    #   J = COSTFUNCTIONREG(theta, X, y, lambda_) computes the cost of using
    #   theta as the parameter for regularized logistic regression and the
    #   gradient of the cost w.r.t. to the parameters.

    # Initialize some useful values
    m = len(y) # number of training examples
    lambda_ = float(lambda_)

    # You need to return the following variables correctly
    J = 0
    grad = zeros(size(theta))

    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost of a particular choice of theta.
    #               You should set J to the cost.
    #               Compute the partial derivatives and set grad to the partial
    #               derivatives of the cost w.r.t. each parameter in theta



    # =============================================================

    return J, grad
