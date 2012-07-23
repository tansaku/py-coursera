from warmUpExercise import *
import unittest
from numpy import *
# TODO - really not sure how to get numpy pulled in ...

class TestWarmUpExercise(unittest.TestCase):
  def setUp(self):
    pass
       
  def testWarmUp(self):
    self.assertEquals(warmUpExercise(),array([]))
