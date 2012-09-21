import nose
from numpy import *
from numpy.testing import *

from gradientDescentMulti import gradientDescentMulti

def testGradientDescentMulti1():
    X = array([[1.,0.]])
    y = array([0.])
    theta = array([0.,0.])
    th = gradientDescentMulti(X, y, theta, 0, 0)[0]
    assert_array_equal(th, theta)

def testGradientDescentMulti2():
    X = array([[1.,0.]])
    y = array([0.])
    theta = array([0.,0.])
    th = gradientDescentMulti(X, y, theta, 1, 10)[0]
    assert_array_equal(th, theta)

def testGradientDescentMulti3():
    X = column_stack((ones(10), arange(10)))
    y = arange(10)*2
    theta = array([1.,2.])
    th = gradientDescentMulti(X, y, theta, 1, 1)[0]
    assert_array_almost_equal(th, array([0.,-2.5]))

def testGradientDescentMulti4():
    X = column_stack((ones(10), arange(10)))
    y = arange(10)*2
    theta = array([1.,2.])
    th = gradientDescentMulti(X, y, theta, 0.05, 100)[0]
    assert_array_almost_equal(th, array([0.2353, 1.9625]), decimal=3)

def testGradientDescentMulti5():
    X = column_stack((ones(101), linspace(0,10,101)))
    y = sin(linspace(0,10,101))
    theta = array([1.,-1.])
    th = gradientDescentMulti(X, y, theta, 0.05, 100)[0]
    assert_array_almost_equal(th, array([0.5132, -0.0545]), decimal=3)

def testgGadientDescentMulti6():
    X = array([[1., 0., 0.]])
    y = array([0.])
    theta = array([1.,2.,3.])
    th = gradientDescentMulti(X, y, theta, 0, 0)[0]
    assert_array_equal(th, theta)

def testGradientDescentMulti7():
    X = column_stack((ones(10), arange(10), arange(10)))
    y = arange(10)*2
    theta = array([0.,0.,0.])
    th = gradientDescentMulti(X, y, theta, 1, 1)[0]
    assert_array_almost_equal(th, array([9.,57.,57.]))

def testGradientDescentMulti8():
    X = column_stack((ones(10), sin(arange(10)), cos(arange(10)), linspace(0.3,0.7,10)))
    y = arange(10)
    theta = array([1.,2.,3.,4.])
    th = gradientDescentMulti(X, y, theta, 0.05, 100)[0]
    assert_array_almost_equal(th, array([1.6225,  0.39764, -0.39422,  5.7765]), decimal=3)


if __name__ == '__main__':
    nose.runmodule()