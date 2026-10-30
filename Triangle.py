# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """


   # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    # UPDATE: moved integer check to front to prevent type misassignment errors
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # UPDATE: changed 'b <= b' to 'b <= 0' 
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly greater than the third side
    # or the specified shape is not a triangle
    # UPDATE: changed minus signs to plus signs and >= to <=, and fixed comment wording
    # UPDATE 2: added not at front and replaced ors with ands to fix faulty logic
    if not ((a <= (b + c)) and (b <= (a + c)) and (c <= (a + b))):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    # UPDATE: removed redundant 'b == a', and added 'b == c' and 'c == a'
    if a == b and b == c and c == a:
        return 'Equilateral'
    # UPDATE: added cases for if sides a or b are the hypotenuse, and replaced * with ^
    elif (((a ^ 2) + (b ^ 2)) == (c ^ 2)) or (((a ^ 2) + (c ^ 2)) == (b ^ 2)) or (((c ^ 2) + (b ^ 2)) == (a ^ 2)):
        return 'Right'
    # UPDATE: changed redundant '(a != b)' to '(c != a)'
    elif (a != b) and  (b != c) and (c != a):
        return 'Scalene'
    else:
        return 'Isoceles'
