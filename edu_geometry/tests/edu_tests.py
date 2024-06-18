#import unittest
from edu_geometry import circle
from edu_geometry import rectangle


class unitedTestSuite(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'llll','wrong upper')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    def test_circle_area(self):
        self.assertEqual(circle.circle_area(1), -2,'wrong circle area') 

    def test_rectangle_area(self):
        assert rectangle.rectangle_area(1, 2) == 2

    def test_rectangle_perimeter(self):
        assert rectangle.rectangle_perimeter(1, 2) == 16

    def test_circle_circumference(self):
        assert circle.circle_circumference(1) == 6.283185307179586

if __name__ == "__main__":
    unitedTestSuite.main()

