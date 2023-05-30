import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

# ADD METHOD
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

# SUBSTRACT METHOD
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(1, self.calc.substract(1, 0))
        self.assertEqual(-1, self.calc.substract(-1, 0))
        self.assertEqual(-3, self.calc.substract(-1, 2))

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

# DIVIDE METHOD
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

# MULTIPLY METHOD
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

# POWER METHOD    
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(1, 0))
        self.assertEqual(1, self.calc.power(-1, 0))
        self.assertEqual(4, self.calc.power(-2, 2))

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())
    
# SQUARE ROOT METHOD
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.sqrt(4))
        self.assertEqual(1, self.calc.sqrt(1))
        self.assertEqual(0, self.calc.sqrt(0))

    def test_sqrt_method_fails_with_negative_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, -1)

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "2", 2)
        self.assertRaises(TypeError, self.calc.sqrt, 2, "2")
        self.assertRaises(TypeError, self.calc.sqrt, "2", "2")
        self.assertRaises(TypeError, self.calc.sqrt, None, 2)
        self.assertRaises(TypeError, self.calc.sqrt, 2, None)
        self.assertRaises(TypeError, self.calc.sqrt, object(), 2)
        self.assertRaises(TypeError, self.calc.sqrt, 2, object())

# LOG BASE 10 METHOD    
    def test_log_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.log(100))
        self.assertEqual(4, self.calc.log(10000))

    def test_log_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log, "2", 2)
        self.assertRaises(TypeError, self.calc.log, 2, "2")
        self.assertRaises(TypeError, self.calc.log, "2", "2")
        self.assertRaises(TypeError, self.calc.log, None, 2)
        self.assertRaises(TypeError, self.calc.log, 2, None)
        self.assertRaises(TypeError, self.calc.log, object(), 2)
        self.assertRaises(TypeError, self.calc.log, 2, object())

    def test_log_method_fails_with_negative_parameter(self):
        self.assertRaises(TypeError, self.calc.log, -1)

    def test_log_method_fails_with_zero(self):
        self.assertRaises(TypeError, self.calc.log, 0)

# CHECK TYPES METHOD    
    def test_check_types_n1_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.check_types_n1, "2")
        self.assertRaises(TypeError, self.calc.check_types_n1, None)
        self.assertRaises(TypeError, self.calc.check_types_n1, object())
    
    def test_check_types_n2_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.check_types_n2, "2")
        self.assertRaises(TypeError, self.calc.check_types_n2, None)
        self.assertRaises(TypeError, self.calc.check_types_n2, object())

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
