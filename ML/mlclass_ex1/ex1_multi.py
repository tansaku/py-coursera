## Machine Learning Online Class
#  Exercise 1: Linear regression with multiple variables

#  Instructions
#  ------------
#
#  This file contains code that helps you get started on the
#  linear regression exercise.
#
#  You will need to complete the following functions in this
#  exericse:
#
#     warmUpExercise.m
#     plotData.m
#     gradientDescent.m
#     computeCost.m
#     gradientDescentMulti.m
#     computeCostMulti.m
#     featureNormalize.m
#     normalEqn.m
#
#  For this part of the exercise, you will need to change some
#  parts of the code below for various experiments (e.g., changing
#  learning rates).
#

from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import axes3d, Axes3D
from mlclass_ex1 import *

## Initialization

## ================ Part 1: Feature Normalization ================

print 'Loading data...'

# load data
data = loadtxt('./ex1data2.txt', delimiter=',')
X = data[:,:2]
y = data[:, 2]
m = len(y)

# Print out some data points
print 'First 10 examples from the dataset:'
for i in range(10):
    print ' x = [%.0f, %.0f], y = %.0f' % (X[i,0], X[i,1], y[i])

print('Program paused. Press enter to continue.')
raw_input()

# Scale features and set them to zero mean
print 'Normalizing Features ...'

X, mu, sigma = featureNormalize(X)

# Add intercept term to X
X = column_stack((ones(m), X))


## ================ Part 2: Gradient Descent ================

# ====================== YOUR CODE HERE ======================
# Instructions: We have provided you with the following starter
#               code that runs gradient descent with a particular
#               learning rate (alpha).
#
#               Your task is to first make sure that your functions -
#               computeCost and gradientDescent already work with
#               this starter code and support multiple variables.
#
#               After that, try running gradient descent with
#               different values of alpha and see which one gives
#               you the best result.
#
#               Finally, you should complete the code at the end
#               to predict the price of a 1650 sq-ft, 3 br house.
#
# Hint: By using the 'hold(True)' command, you can plot multiple
#       graphs on the same figure.
#
# Hint: At prediction, make sure you do the same feature normalization.
#

print 'Running gradient descent ...'

# Choose some alpha value
alpha = 0.01
num_iters = 400

# Init Theta and Run Gradient Descent
theta = zeros(3)
theta, J_history = gradientDescentMulti(X, y, theta, alpha, num_iters);

# Plot the convergence graph
fig = figure()
plot(J_history, '-b', linewidth=2)
xlabel('Number of iterations')
ylabel('Cost J')
fig.show()

# Display gradient descent's result
print 'Theta computed from gradient descent:'
for t in theta: print t
print

# Estimate the price of a 1650 sq-ft, 3 br house
# ====================== YOUR CODE HERE ======================
# Recall that the first column of X is all-ones. Thus, it does
# not need to be normalized.
price = 0 # You should change this


# ============================================================

print 'Predicted price of a 1650 sq-ft, 3 br house ' \
      '(using gradient descent):\n $%f\n' %  price

print 'Program paused. Press enter to continue.'
raw_input()

## ================ Part 3: Normal Equations ================
print 'Solving with normal equations...'

# ====================== YOUR CODE HERE ======================
# Instructions: The following code computes the closed form
#               solution for linear regression using the normal
#               equations. You should complete the code in
#               normalEqn.m
#
#               After doing so, you should complete this code
#               to predict the price of a 1650 sq-ft, 3 br house.
#

## Load Data
data = loadtxt('./ex1data2.txt', delimiter=',')
X = data[:,:2]
y = data[:, 2]
m = len(y)

# Add intercept term to X
X = column_stack((ones(m), X))

# Calculate the parameters from the normal equation
theta = normalEqn(X, y)

# Display normal equation's result
print 'Theta computed from the normal equations:'
for t in theta: print t
print


# Estimate the price of a 1650 sq-ft, 3 br house
# ====================== YOUR CODE HERE ======================
price = 0 # You should change this


# ============================================================

print 'Predicted price of a 1650 sq-ft, 3 br house ' \
      '(using normal equations):\n $%f' % price

