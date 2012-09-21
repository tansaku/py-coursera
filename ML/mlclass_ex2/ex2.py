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

from plotData import plotData
from costFunction import costFunction
from plotDecisionBoundary import plotDecisionBoundary
from sigmoid import sigmoid
from predict import predict


## Load Data
#  The first two columns contains the exam scores and the third column
#  contains the label.

data = loadtxt('ex2data1.txt', delimiter=',')
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
print grad

print '\nProgram paused. Press enter to continue.'
raw_input()


## ============= Part 3: Optimizing using fminunc  =============
#  In this exercise, you will use a built-in function (fminunc) to find the
#  optimal parameters theta.

#  Run minimize to obtain the optimal theta
res = optimize.minimize(costFunction, initial_theta, args=(X,y), \
                        method='BFGS', jac=True, options={'maxiter':400})

#  Extract theta and the cost from the result of minimize
theta = res.x
cost = res.fun

# Print theta to screen
print 'Cost at theta found by minimize: ', cost
print 'theta:', theta

# Plot Boundary
fig = plotDecisionBoundary(theta, X, y)

# Put some labels
hold(True)
xlabel('Exam 1 score')
ylabel('Exam 2 score')
hold(False)
fig.show()

print '\nProgram paused. Press enter to continue.'
raw_input()


## ============== Part 4: Predict and Accuracies ==============
#  After learning the parameters, you'll like to use it to predict the outcomes
#  on unseen data. In this part, you will use the logistic regression model
#  to predict the probability that a student with score 45 on exam 1 and
#  score 85 on exam 2 will be admitted.
#
#  Furthermore, you will compute the training and test set accuracies of
#  our model.
#
#  Your task is to complete the code in predict.m

#  Predict probability for a student with score 45 on exam 1
#  and score 85 on exam 2

prob = sigmoid(dot([1, 45, 85],theta))
print 'For a student with scores 45 and 85, we predict an admission ' \
      'probability of %f\n' % prob

# Compute accuracy on our training set
p = predict(theta, X)

print 'Train Accuracy: %f\n' % (mean(p == y) * 100)

print '\nProgram paused. Press enter to continue.'
raw_input()

