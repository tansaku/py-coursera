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
from mpl_toolkits.mplot3d import axes3d, Axes3D
from mlclass_ex2 import *

## Load Data
#  The first two columns contains the exam scores and the third column
#  contains the label.

data = loadtxt('ex2data1.txt', delimiter=',');
X = data[:,:2]
y = data[:, 2]

## ==================== Part 1: Plotting ====================
# We start the exercise by first plotting the data to understand the
#  the problem we are working with.

print 'Plotting data with + indicating (y = 1) examples and o '\
      'indicating (y = 0) examples.\n'

fig = plotData(X, y)

# Put some labels
hold(True)
# Labels and Legend
xlabel('Exam 1 score')
ylabel('Exam 2 score')

# Specified in plot order
legend(('Admitted', 'Not admitted'), numpoints=1)
fig.show()
hold(False)

print '\nProgram paused. Press enter to continue.'
raw_input()

## ============ Part 2: Compute Cost and Gradient ============
#  In this part of the exercise, you will implement the cost and gradient
#  for logistic regression. You neeed to complete the code in
#  costFunction.m

#  Setup the data matrix appropriately, and add ones for the intercept term
m, n = shape(X)

# Add intercept term to x and X_test
X = column_stack((ones(m), X))

# Initialize fitting parameters
initial_theta = zeros(n + 1)

# Compute and display initial cost and gradient
cost, grad = costFunction(initial_theta, X, y)

print 'Cost at initial theta (zeros): ', cost
print 'Gradient at initial theta (zeros):'
print '', grad

print '\nProgram paused. Press enter to continue.'
raw_input()




