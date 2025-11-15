import unittest
import math
from calculator import ScientificCalculator

class TestScientificCalculator(unittest.TestCase):
    """Unit tests for Scientific Calculator"""
    
    def setUp(self):
        """Set up test calculator instance"""
        self.calc = ScientificCalculator()
    
    Square Root Tests
    def test_square_root_positive(self):
        """Test square root of positive number"""
        result = self.calc.square_root(16)
        self.assertEqual(result, 4.0)
    
    def test_square_root_zero(self):
        """Test square root of zero"""
        result = self.calc.square_root(0)
        self.assertEqual(result, 0.0)
    
    def test_square_root_negative(self):
        """Test square root raises error for negative number"""
        with self.assertRaises(ValueError):
            self.calc.square_root(-4)
    
    # Factorial Tests
    def test_factorial_positive(self):
        """Test factorial of positive integer"""
        result = self.calc.factorial(5)
        self.assertEqual(result, 120)
    
    def test_factorial_zero(self):
        """Test factorial of zero"""
        result = self.calc.factorial(0)
        self.assertEqual(result, 1)
    
    def test_factorial_negative(self):
        """Test factorial raises error for negative number"""
        with self.assertRaises(ValueError):
            self.calc.factorial(-5)
    
    # Natural Log Tests
    def test_natural_log_positive(self):
        """Test natural log of positive number"""
        result = self.calc.natural_log(math.e)
        self.assertAlmostEqual(result, 1.0, places=5)
    
    def test_natural_log_zero(self):
        """Test natural log raises error for zero"""
        with self.assertRaises(ValueError):
            self.calc.natural_log(0)
    
    def test_natural_log_negative(self):
        """Test natural log raises error for negative number"""
        with self.assertRaises(ValueError):
            self.calc.natural_log(-5)
    
    # Power Tests
    def test_power_positive_exponent(self):
        """Test power with positive exponent"""
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8.0)
    
    def test_power_zero_exponent(self):
        """Test power with zero exponent"""
        result = self.calc.power(5, 0)
        self.assertEqual(result, 1.0)
    
    def test_power_negative_exponent(self):
        """Test power with negative exponent"""
        result = self.calc.power(2, -2)
        self.assertAlmostEqual(result, 0.25, places=5)

if __name__ == '__main__':
    unittest.main()
