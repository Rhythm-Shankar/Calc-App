import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertAlmostEqual(calc.add(2.5, 0.5), 3.0)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 3), 2)
        self.assertEqual(calc.subtract(-1, -1), 0)
        self.assertAlmostEqual(calc.subtract(3.5, 1.2), 2.3)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-1, 5), -5)
        self.assertAlmostEqual(calc.multiply(2.5, 2), 5.0)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertAlmostEqual(calc.divide(7, 2), 3.5)
        with self.assertRaises(ValueError):
            calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()

