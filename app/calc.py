import app
import math

class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types_n1(x)
        self.check_types_n2(y)
        return x + y

    def substract(self, x, y):
        self.check_types_n1(x)
        self.check_types_n2(y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types_n1(x)
        self.check_types_n2(y)
        return x * y

    def divide(self, x, y):
        self.check_types_n1(x)
        self.check_types_n2(y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types_n1(x)
        self.check_types_n2(y)
        return x ** y

    def sqrt(self, x):
        self.check_types_n1(x)
        if x < 0:
            raise TypeError("Square root on negative numbers is not possible")

        return x ** 0.5

    def log(self, x):
        self.check_types_n1(x)
        if x < 0 or x == 0:
            raise TypeError("Logarithm on negative numbers and zero is not possible")

        return math.log10(x)

    def check_types_n1(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter x must be numbers")

    def check_types_n2(self, y):
        if not isinstance(y, (int, float)):
            raise TypeError("Parameter y must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
