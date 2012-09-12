## Machine Learning Online Class - Exercise 2: Logistic Regression
#
#  Instructions
#  ------------
#
#  This file contains code that helps you get started on the logistic
#  regression exercise. You will need to complete the following functions
#  in this exericse:
#
#     sigmoid.m
#     costFunction.m
#     predict.m
#     costFunctionReg.m
#
#  For this exercise, you will not need to change any code in this file,
#  or any other files other than those mentioned above.
#

from numpy import *
from matplotlib.pyplot import *
from scipy import optimize
from mlclass_ex2 import *

## Load Data
#  The first two columns contains the X values and the third column
#  contains the label (y).

data = loadtxt('ex2data2.txt', delimiter=',');
X = data[:,:2]
y = data[:, 2]

fig = plotData(X, y)

# Put some labels
hold(True)
# Labels and Legend
xlabel('Microchip Test 1')
ylabel('Microchip Test 2')

# Specified in plot order
legend(('y = 1', 'y = 0'), numpoints=1)
hold(False)
fig.show()



## =========== Part 1: Regularized Logistic Regression ============
#  In this part, you are given a dataset with data points that are not
#  linearly separable. However, you would still like to use logistic
#  regression to classify the data points.
#
#  To do so, you introduce more features to use -- in particular, you add
#  polynomial features to our data matrix (similar to polynomial
#  regression).
#

# Add Polynomial Features

# Note that mapFeature also adds a column of ones for us, so the intercept
# term is handled
X = mapFeature(X[:,0], X[:,1])

# Initialize fitting parameters
initial_theta = zeros(size(X, 1))

# Set regularization parameter lambda to 1
lambda_ = 1.

# Compute and display initial cost and gradient for regularized logistic
# regression
cost, grad = costFunctionReg(initial_theta, X, y, lambda_)

print 'Cost at initial theta (zeros):', cost

print '\nProgram paused. Press enter to continue.'
raw_input()


## ============= Part 2: Regularization and Accuracies =============
#  Optional Exercise:
#  In this part, you will get to try different values of lambda and
#  see how regularization affects the decision coundart
#
#  Try the following values of lambda (0, 1, 10, 100).
#
#  How does the decision boundary change when you vary lambda? How does
#  the training set accuracy vary?
#

# Initialize fitting parameters
initial_theta = zeros(size(X, 1))

# Set regularization parameter lambda to 1 (you should vary this)
lambda_ = 1.

# Optimize
res = optimize.minimize(costFunctionReg, initial_theta, args=(X,y,lambda_), \
                        method='BFGS', jac=True, options={'maxiter':400})
theta = res.x
cost = res.fun

# Plot Boundary
fig = plotDecisionBoundary(theta, X, y)
hold(True)
title('lambda = %g' % lambda_)

# Labels and Legend
xlabel('Microchip Test 1')
ylabel('Microchip Test 2')

legend(('y = 1', 'y = 0', 'Decision boundary'), numpoints=1)
hold(False)
fig.show()

# Compute accuracy on our training set
p = predict(theta, X)

print 'Train Accuracy: %f\n' % (mean(p == y) * 100)
print '\nProgram paused. Press enter to continue.'
raw_input()
