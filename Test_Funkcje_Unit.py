import unittest
import math
import Funkcje

class TestCircleArea(unittest.TestCase):

    def test_area(self):
        """Test Ares"""
        self.assertAlmostEqual(Funkcje.circle_area(1), math.pi)
        self.assertEqual(Funkcje.circle_area(0), 0)
        self.assertAlmostEqual(Funkcje.circle_area(2.1), math.pi * 2.1**2)

    def test_value(self):
        self. assertRaises(ValueError, Funkcje.circle_area, -2)

    def test_type(self):
        self.assertRaises(TypeError, Funkcje.circle_area, 3+5j)
        self.assertRaises(TypeError, Funkcje.circle_area, True)
        self.assertRaises(TypeError, Funkcje.circle_area, "radius")