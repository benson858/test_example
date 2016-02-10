#
# https://confluence.jetbrains.com/display/PYH/Creating+and+running+a+Python+unit+test
#

import unittest
from solver import Solver


class TestSolver(unittest.TestCase):
    def test_negative_discr(self):
        s = Solver
        self.assertRaises(Exception,s.demo,2,1,2)

    def test_demo(self):
        pass
        #self.fail()

if __name__ == '__main__':
     unittest.main()
