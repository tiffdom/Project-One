import unittest
from main import *

class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(a.circle(3), 9.42)
        self.assertEqual(a.square(2), 4.0)
        self.assertEqual(a.rectangle(2, 6), 12.0)
        self.assertEqual(a.triangle(3, 6), 9.0, msg='Test 1 failed.')

    def test_perimeter(self):
        self.assertEqual(p.circle(3), 18.84)
        self.assertEqual(p.square(2), 8.0)
        self.assertEqual(p.rectangle(2, 6), 16.0)
        self.assertEqual(p.triangle(2, 3, 6), 11.0, msg='Test 2 failed.')

    def test_exceptions(self):
        self.assertRaises(TypeError, a.circle, 't')
        self.assertRaises(TypeError, a.square, 'a')
        self.assertRaises(TypeError, a.rectangle, 'a', 't')
        self.assertRaises(TypeError, a.triangle, 'a', 't', msg='Test 3 Failed.')


if __name__ == '__main__':
    unittest.main()
