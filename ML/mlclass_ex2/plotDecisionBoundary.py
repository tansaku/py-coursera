from numpy import *
from matplotlib.pyplot import *
from mlclass_ex2 import *

def plotDecisionBoundary(theta, X, y):
    #PLOTDECISIONBOUNDARY Plots the data points X and y into a new figure with
    #the decision boundary defined by theta
    #   PLOTDECISIONBOUNDARY(theta, X,y) plots the data points with + for the
    #   positive examples and o for the negative examples. X is assumed to be
    #   a either
    #   1) Mx3 matrix, where the first column is an all-ones column for the
    #      intercept.
    #   2) MxN, N>3 matrix, where the first column is all-ones

    # Plot Data
    fig = plotData(X[:,1:], y)
    hold(True)

    if size(X, 1) <= 3:
        # Only need 2 points to define a line, so choose two endpoints
        plot_x = array([min(X[:,1])-2,  max(X[:,1])+2])

        # Calculate the decision boundary line
        plot_y = (-1/theta[2]) * (theta[1] * plot_x + theta[0])

        # Plot, and adjust axes for better viewing
        plot(plot_x, plot_y)

        # Legend, specific for the exercise
        legend(('Admitted', 'Not admitted', 'Decision Boundary'), numpoints=1)
        axis([30, 100, 30, 100])
    else:
        u = linspace(-1, 1.5, 50)

        # Evaluate z = theta*x over the grid
        z = frompyfunc(lambda x,y: mapFeature(x,y).dot(theta), 2, 1).outer(u,u)

        z = z.T # important to transpose z before calling contour

        # Plot z = 0
        # Notice you need to specify the level as [0]
        contour(u, u, z, [0], linewidth=2)

    hold(False)

    return fig
