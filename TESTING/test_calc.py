import unittest
import calc


class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10,15), 25)
        self.assertEqual(calc.add(-1,15), 14)
        self.assertEqual(calc.add(-5,-5), -10)
        self.assertEqual(calc.add(-5,5), 0)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,15), -5)
        self.assertEqual(calc.subtract(15,10), 5)
        self.assertEqual(calc.subtract(-15,-10), -5)
        self.assertEqual(calc.subtract(15,-10), 25)
        self.assertEqual(calc.subtract(-15,10), -25)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,15), 150)
        self.assertEqual(calc.multiply(-10,15), -150)
        self.assertEqual(calc.multiply(10,-15), -150)
        self.assertEqual(calc.multiply(-10,-15), 150)

    def test_divide(self):
        self.assertEqual(calc.divide(10,15), 2/3)
        self.assertEqual(calc.divide(10,2), 5)
        self.assertEqual(calc.divide(10,-5), -2)
        self.assertEqual(calc.divide(-10,15), -2/3)
        
        # self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            calc.divide(10,0)


if __name__ == "__main__":
    unittest.main()