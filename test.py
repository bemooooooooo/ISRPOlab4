import unittest
import rectangle, circle, square, triangle

class RectangleTestCase(unittest.TestCase):
    '''
    Tests the perimeter and area functions for rectangular
    '''
    def test_zero_area(self):
        '''
        Test zero multiply zero in area function
        '''
        res = rectangle.area(0,0)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 0)

    def test_square_area(self):
        '''
        Test if rectangle was a square
        '''
        res = rectangle.area(10,10)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        '''
        Tets if a and b were zero
        '''
        res = rectangle.perimeter(0,0)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 0)

    def test_zero_one_perimeter(self):
        '''
        Test if a and b were pair of 0 and 1
        '''
        res = rectangle.perimeter(0,1)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 2)

    def test_square_perimeter(self):
        '''
        Test if rectangular was a square
        '''
        res = rectangle.perimeter(10,10)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 40)


class CircleTestCase(unittest.TestCase):
    '''
    Tests the perimeter and area functions for circle
    '''
    def test_zero_area(self):
        '''
        Test zero multiply zero in area function
        '''
        res = circle.area(0)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 0)

    def test_area(self):
        '''
        Test multiplying in area function
        '''
        res = circle.area(153)
        '''
        Compare the output and the answer we calculated
        '''
        self.assertEqual(res, 73541.54242788347)

    def test_zero_perimeter(self):
        '''
        Tets if r was zero
        '''
        res = circle.perimeter(0)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 0)

    def test_perimeter(self):
        '''
        Test multiplying in perimeter function
        '''
        res = circle.perimeter(153)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 961.3273519984767)


class SquareTestCase(unittest.TestCase):
    '''
    Tests the perimeter and area functions for square
    '''
    def test_zero_area(self):
        '''
        Test zero multiply zero in area function
        '''
        res = square.area(0)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 0)

    def test_area(self):
        '''
        Test multiplying in area function
        '''
        res = square.area(153)
        '''
        Compare the output and the answer we calculated
        '''
        self.assertEqual(res, 23409)

    def test_zero_perimeter(self):
        '''
        Tets if a was zero
        '''
        res = square.perimeter(0)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 0)

    def test_perimeter(self):
        '''
        Test multiplying in perimeter function
        '''
        res = square.perimeter(153)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 612)


class TriangleTestCase(unittest.TestCase):
    '''
    Tests the perimeter and area functions for triangle
    '''
    def test_zero_area(self):
        '''
        Test zero multiply zero in area function
        '''
        res = triangle.area(0, 0)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 0)

    def test_height_zero_area(self):
        '''
        Test if height is zero
        '''
        res = triangle.area(153, 0)
        '''
        Compare the output and the answer we calculated
        '''
        self.assertEqual(res, 0)

    def test_side_zero_area(self):
        '''
        Test if side is zero
        '''
        res = triangle.area(0, 153)
        '''
        Compare the output and the answer we calculated
        '''
        self.assertEqual(res, 0)

    def test_area(self):
        '''
        Test multiplying in area function
        '''
        res = triangle.area(153, 93)
        '''
        Compare the output and the answer we calculated
        '''
        self.assertEqual(res, 7114.5)

    def test_zero_perimeter(self):
        '''
        Tets zero add zero add zero
        '''
        res = triangle.perimeter(0,0,0)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 0)

    def test_one_zero_perimeter(self):
        '''
        Tets something add zero add zero
        '''
        res1 = triangle.perimeter(153,0,0)
        res2 = triangle.perimeter(0, 153, 0)
        res3 = triangle.perimeter(0, 0, 153)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res1, 153)
        self.assertEqual(res2, 153)
        self.assertEqual(res3, 153)

    def test_perimeter(self):
        '''
        Test adding in perimeter function
        '''
        res = triangle.perimeter(153, 153, 153)
        '''
        Compares the output and the answer we calculated
        '''
        self.assertEqual(res, 459)
