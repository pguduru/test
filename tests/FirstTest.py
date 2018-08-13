import unittest
import sys
sys.path.insert(0, '../')
from First import *

class TestFirst(unittest.TestCase):

    def setUp(self):
        pass
 
    def test_sum(self):
        f = First([3,4])
        self.assertEqual( f.numsum(), 7)



if __name__ == '__main__':
    unittest.main()

