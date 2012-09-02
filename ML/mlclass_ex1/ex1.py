## Machine Learning Online Class - Exercise 1: Linear Regression

#  Instructions
#  ------------
#
#  This file contains code that helps you get started on the
#  linear exercise. You will need to complete the following functions
#  in this exericse:
#
#     warmUpExercise.py
#     plotData.py
#     gradientDescent.py
#     computeCost.py
#     gradientDescentMulti.py
#     computeCostMulti.py
#     featureNormalize.py
#     normalEqn.py
#
#  For this exercise, you will not need to change any code in this file,
#  or any other files other than those mentioned above.
#
# x refers to the population size in 10,000s
# y refers to the profit in $10,000s
#

import pdb
## Initialization
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import axes3d, Axes3D
from mlclass_ex1 import *
# is there any equivalent to "clear all; close all; clc"?

## ==================== Part 1: Basic Function ====================
# Complete warmUpExercise.py
print 'Running warmUpExercise ... '
print '5x5 Identity Matrix: '
print warmUpExercise()

print('Program paused. Press enter to continue.')
raw_input()


## ======================= Part 2: Plotting =======================
print 'Plotting Data ...'
data = loadtxt('./ex1data1.txt', delimiter=',')
X = data[:, 0]; y = data[:, 1]
m = len(y) # number of training examples

# Plot Data
# Note: You have to complete the code in plotData.py
firstPlot = plotData(X, y)
firstPlot.show()

print 'Program paused. Press enter to continue.'
raw_input()



## =================== Part 3: Gradient descent ===================
print 'Running Gradient Descent ...'

X = hstack((ones((m, 1)), vstack(data[:,0]))) # Add a column of ones to x
theta = zeros(2) # initialize fitting parameters

# Some gradient descent settings
iterations = 1500
alpha = 0.01

# compute and display initial cost
print computeCost(X, y, theta)

# run gradient descent
(theta, J_history) = gradientDescent(X, y, theta, alpha, iterations)
#pdb.set_trace()

# print theta to screen
print 'Theta found by gradient descent: '
print '%f %f \n' % (theta[0], theta[1])

# Plot the linear fit
hold(True); # keep previous plot visible
plot(X[:,1], X.dot(theta), '-')
legend(('Training data', 'Linear regression'))
firstPlot.show()
# not sure how to avoid overlaying any more plots on this figure - call figure()?

# Predict values for population sizes of 35,000 and 70,000
predict1 = array([1, 3.5]).dot(theta)
#pdb.set_trace()
print 'For population = 35,000, we predict a profit of %f\n' % (predict1 * 10000.)
predict2 = array([1, 7]).dot(theta)
print 'For population = 70,000, we predict a profit of %f\n' % (predict2 * 10000.)

print 'Program paused. Press enter to continue.\n'
raw_input()


## ============= Part 4: Visualizing J(theta_0, theta_1) =============
print 'Visualizing J(theta_0, theta_1) ...\n'

# Grid over which we will calculate J
theta0_vals = linspace(-10, 10, 100)
theta1_vals = linspace(-1, 4, 100)

# initialize J_vals to a matrix of 0's
J_vals = zeros((len(theta0_vals), len(theta1_vals)))

# Fill out J_vals
for i in range(len(theta0_vals)):
    for j in range(len(theta1_vals)):
        t = array((theta0_vals[i], theta1_vals[j]))
        J_vals[i][j] = computeCost(X, y, t)


# Because of the way meshgrids and mplot3d work, we need to transpose
# J_vals before plotting the surface, or else the axes will be flipped
J_vals = J_vals.T
# Surface plot
fig = figure()
ax = Axes3D(fig)
#pdb.set_trace()
sX, sY = meshgrid(theta0_vals, theta1_vals)
ax.plot_surface(sX, sY, J_vals, rstride=3, cstride=3, cmap=cm.jet, linewidth=0)
xlabel('\\theta_0')
ylabel('\\theta_1')
fig.show()

# Contour plot
fig = figure()
# Plot J_vals as 20 contours spaced logarithmically between 0.01 and 1000
contour(sX, sY, J_vals, logspace(-2, 2, 20))
plot(theta[0], theta[1], 'rx', markersize=10, linewidth=2)
xlabel('\\theta_0')
ylabel('\\theta_1')
fig.show()

print 'Program paused. Press enter to continue. Note figures will disappear when Python process ends\n'
raw_input()



