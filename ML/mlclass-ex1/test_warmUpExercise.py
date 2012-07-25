from warmUpExercise import *
import unittest
from numpy import *
from numpy.testing import *

class TestWarmUpExercise(unittest.TestCase):
  def setUp(self):
    pass
       
  def testWarmUp(self):
    '''trying to compare arrays but see http://stackoverflow.com/questions/1322380/gotchas-where-numpy-differs-from-straight-python
    and http://stackoverflow.com/questions/3302949/whats-the-best-way-to-assert-for-scipy-array-equality'''
    assert_array_equal(warmUpExercise(), array([]))
    self.assertTrue((warmUpExercise() == array([])).all())
    #self.assertEquals(array([0,0]), array([0,0]))
    #self.assertTrue(warmUpExercise() == array([]))
