# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(203,4,5),'InvalidInput','Side a is too large')

    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(3,204,5),'InvalidInput','Side b is too large')

    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle(3,4,205),'InvalidInput','Side c is too large')

    def testInvalidInputD(self): 
        self.assertEqual(classifyTriangle(-3,4,5),'InvalidInput','Side a is negative')

    def testInvalidInputE(self): 
        self.assertEqual(classifyTriangle(3,-4,5),'InvalidInput','Side b is negative')

    def testInvalidInputF(self): 
        self.assertEqual(classifyTriangle(3,4,-5),'InvalidInput','Side c is negative')

    def testInvalidInputG(self): 
        self.assertEqual(classifyTriangle("a",4,5),'InvalidInput','Side a is not an integer')

    def testInvalidInputH(self): 
        self.assertEqual(classifyTriangle(3,4.5,5),'InvalidInput','Side b is not an integer')

    def testInvalidInputI(self): 
        self.assertEqual(classifyTriangle(3,4,"c"),'InvalidInput','Side c is not an integer')

    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(1,2,5),'NotATriangle','1 + 2 < 5, so cannot be triangle')

    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(5,1,2),'NotATriangle','1 + 2 < 5, so cannot be triangle')

    def testNotATriangleC(self): 
        self.assertEqual(classifyTriangle(2,5,1),'NotATriangle','1 + 2 < 5, so cannot be triangle')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,3),'Isoceles','3,4,3 is an Isosceles triangle')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(4,3,3),'Isoceles','4,3,3 is an Isosceles triangle')

    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(3,3,4),'Isoceles','3,3,4 is an Isosceles triangle')

    def testEquilateralTriangle(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is an Equilateral triangle')

    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(5,6,7),'Scalene','5,6,7 is a Scalene triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

