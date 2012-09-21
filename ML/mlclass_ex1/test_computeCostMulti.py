import nose
from numpy import *
from numpy.testing import *

from computeCostMulti import computeCostMulti

def testComputeCostMulti1():
    X = array([[1., 0.]])
    y = array([0.])
    theta = array([0., 0.])
    assert_equal(computeCostMulti(X, y, theta), 0)

def testComputeCostMulti2():
    X = column_stack((ones(10), arange(10)))
    y = arange(10)*2
    theta = array([1., 2.])
    assert_almost_equal(computeCostMulti(X, y, theta), 0.5)

def testComputeCostMulti3():
    X = column_stack((ones(101), linspace(0,10,101)))
    y = sin(linspace(0,10,101))
    theta = array([0., 0.])
    assert_almost_equal(computeCostMulti(X, y, theta), 0.23699618)

def testComputeCostMulti4():
    X = column_stack((ones(10), sin(arange(10)), cos(arange(10)), linspace(0.3,0.7,10)))
    y = arange(10)
    theta = array([1., 2., 3., 4.])
    assert_almost_equal(computeCostMulti(X, y, theta), 7.3698431965)

if __name__ == '__main__':
    nose.runmodule()