from src.calc import Calc
import unittest


class TestCalc(unittest.TestCase):
    def setUp(self):
        print("* setUp()")
        self.calc = Calc()

    def test_add(self):
        #Arrange
        a = 3
        b = 2
        r = 5

        print("* test_add()")

        #Act
        result = self.calc.add(a, b)

        #Assert
        self.assertEqual(result, r)

    def test_divide_by_zero(self):
        #Arrange
        a = 10
        b = 0

        print("* test_divide_by_zero()")

        #Act Assert
        with self.assertRaises(ValueError):
            self.calc.divide(a, b)


    def test_multiply(self):
        #Arrange
        a = 2
        b = 3
        r = 6
        print("* test_multiply()")

        #Act
        result = self.calc.multiply(a, b)

        #Assert
        self.assertEqual(result, r)

    def test_subtract(self):
        #Arrange
        a = 7
        b = 2
        r = 5
        print("* test_subtract()")

        #Act
        result = self.calc.subtract(a, b)

        #Assert
        self.assertEqual(result, r)

    def test_divide(self):
        #Arrange
        a = 10
        b = 5
        r = 2
        print("* test_divide()")

        #Act
        result = self.calc.divide(a, b)

        #Assert
        self.assertEqual(result, r)

    def tearDown(self):
        print("* tearDown()")
        self.calc = None

if __name__ == '__main__':
    unittest.main()

