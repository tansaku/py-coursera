import nose
from numpy import *
from numpy.testing import *

from computeCost import computeCost

def testComputeCost1():
    X = array([[1., 0.]])
    y = array([0.])
    theta = array([0., 0.])
    assert_equal(computeCost(X, y, theta), 0)

def testComputeCost2():
    X = column_stack((ones(10), arange(10)))
    y = arange(10)*2
    theta = array([1., 2.])
    assert_almost_equal(computeCost(X, y, theta), 0.5)

def testComputeCost3():
    X = column_stack((ones(101), linspace(0,10,101)))
    y = sin(linspace(0,10,101))
    theta = array([0., 0.])
    assert_almost_equal(computeCost(X, y, theta), 0.23699618)


if __name__ == '__main__':
    nose.runmodule()