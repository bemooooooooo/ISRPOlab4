import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    '''
    Tests the perimeter and area functions for rectangular
    '''
    def test_zero_area(self):
        '''
        Test zero multiply zero in area function
        '''
        res = area(0,0)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 0)

    def test_square_area(self):
        '''
        Test if rectangle was a square
        '''
        res = area(10,10)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        '''
        Tets if a and b were zero
        '''
        res = perimeter(0,0)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 0)

    def test_zero_one_perimeter(self):
        '''
        Test if a and b were pair of 0 and 1
        '''
        res = perimeter(0,1)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 2)

    def test_square_perimeter(self):
        '''
        Test if rectangular was a square
        '''
        res = perimeter(10,10)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 40)
