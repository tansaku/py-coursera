import nose
from numpy import *
from numpy.testing import *

from gradientDescent import gradientDescent

def testGradientDescent1():
    X = array([[1., 0.]])
    y = array([0.])
    theta = array([0.,0.])
    th = gradientDescent(X, y, theta, 0, 0)[0]
    assert_array_equal(th, theta)

def testGradientDescent2():
    X = array([[1.,0.]])
    y = array([0.])
    theta = array([0.,0.])
    th = gradientDescent(X, y, theta, 1, 10)[0]
    assert_array_equal(th, theta)

def testGradientDescent3():
    X = column_stack((ones(10), arange(10)))
    y = arange(10)*2
    theta = array([1.,2.])
    th = gradientDescent(X, y, theta, 1, 1)[0]
    assert_array_almost_equal(th, array([0.,-2.5]))

def testGradientDescent4():
    X = column_stack((ones(10), arange(10)))
    y = arange(10)*2
    theta = array([1.,2.])
    th = gradientDescent(X, y, theta, 0.05, 100)[0]
    assert_array_almost_equal(th, array([0.2353, 1.9625]), decimal=3)

def testGradientDescent5():
    X = column_stack((ones(101), linspace(0,10,101)))
    y = sin(linspace(0,10,101))
    theta = array([1.,-1.])
    th = gradientDescent(X, y, theta, 0.05, 100)[0]
    assert_array_almost_equal(th, array([0.5132, -0.0545]), decimal=3)

if __name__ == '__main__':
    nose.runmodule()