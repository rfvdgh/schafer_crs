import unittest

calc = __import__("57_ut_calc")  # problems with importing 57_ut_calc


# inherting from TestCase give us lots of capabilities
class TestCalc(unittest.TestCase):
    def test_add(self):  # ***naming convention of 'test_' REQUIRED***
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # self.assertRaises(ValueError, calc.divide, 10, 0)
        # alternative use a context manager so you can pass arguments
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


# if didn't want to run in terminal with: python -m unittest 57_ut_test_calc.py
# This will also allow us to run in the editor
if __name__ == "__main__":
    unittest.main()  # this will basically run all of our tests
