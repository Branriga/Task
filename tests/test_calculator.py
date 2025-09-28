
# con unitest
import unittest
from src.calculator import *

class Testcalculator(unittest.TestCase):
  def test_suma(self):
    self.assertEqual(suma(2,3), 5)

  def test_resta(self):
   self.assertEqual(resta(5,3), 2)

if __name__ == '__main__':
  unittest.main()


# con pytest
#from src.calculator import *

#def test_suma(self):
  #self.assertEqual(suma(2,3), 5)

#def test_resta(self):
  #self.assertEqual(resta(5,3), 2)