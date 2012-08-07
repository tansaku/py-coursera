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

## Initialization
from warmUpExercise import *
from plotData import *
from computeCost import *
from gradientDescent import *
# is there any equivalent to "clear all; close all; clc"?

## ==================== Part 1: Basic Function ====================
# Complete warmUpExercise.py 
print 'Running warmUpExercise ... '
print '5x5 Identity Matrix: '
print warmUpExercise()

print('Program paused. Press enter to continue.')
#raw_input()


## ======================= Part 2: Plotting =======================
print 'Plotting Data ...'
data = loadtxt('ex1data1.txt')
X = data[:, 0]; y = data[:, 1]
m = len(y) # number of training examples

# Plot Data
# Note: You have to complete the code in plotData.m
plotData(X, y)

print 'Program paused. Press enter to continue.'
#raw_input()



## =================== Part 3: Gradient descent ===================
print 'Running Gradient Descent ...'

X = hstack((ones((m, 1)), vstack(data[:,0]))) # Add a column of ones to x
theta = zeros((2, 1)) # initialize fitting parameters

# Some gradient descent settings
iterations = 1500
alpha = 0.01

# compute and display initial cost
computeCost(X, y, theta)

# run gradient descent
(theta, J_history) = gradientDescent(X, y, theta, alpha, iterations)

# print theta to screen
print 'Theta found by gradient descent: '
print '%f %f \n' % (theta[0].var(), theta[1].var())

# Plot the linear fit
#hold on; # keep previous plot visible
plot(vstack(X[:,1]), X.dot(theta), '-')
legend(('Training data', 'Linear regression'))
# not sure how to avoid overlaying any more plots on this figure - call figure()?

# Predict values for population sizes of 35,000 and 70,000
# note this it outputting too many times TODO fix this....
predict1 = array([1, 3.5]) *theta
print 'For population = 35,000, we predict a profit of %f\n' % predict1.var()*10000
predict2 = array([1, 7]) * theta
print 'For population = 70,000, we predict a profit of %f\n' % predict2.var()*10000

print 'Program paused. Press enter to continue.\n'
raw_input()
'''
#  ALL BELOW IS TODO


## ============= Part 4: Visualizing J(theta_0, theta_1) =============
print('Visualizing J(theta_0, theta_1) ...\n')

# Grid over which we will calculate J
theta0_vals = linspace(-10, 10, 100);
theta1_vals = linspace(-1, 4, 100);

# initialize J_vals to a matrix of 0's
J_vals = zeros(length(theta0_vals), length(theta1_vals));

# Fill out J_vals
for i = 1:length(theta0_vals)
    for j = 1:length(theta1_vals)
	  t = [theta0_vals(i); theta1_vals(j)];    
	  J_vals(i,j) = computeCost(X, y, t);
    end
end


# Because of the way meshgrids work in the surf command, we need to 
# transpose J_vals before calling surf, or else the axes will be flipped
J_vals = J_vals';
# Surface plot
figure;
surf(theta0_vals, theta1_vals, J_vals)
xlabel('\theta_0'); ylabel('\theta_1');

# Contour plot
figure;
# Plot J_vals as 15 contours spaced logarithmically between 0.01 and 100
contour(theta0_vals, theta1_vals, J_vals, logspace(-2, 3, 20))
xlabel('\theta_0'); ylabel('\theta_1');
hold on;
plot(theta(1), theta(2), 'rx', 'MarkerSize', 10, 'LineWidth', 2);

'''
