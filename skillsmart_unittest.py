import unittest
import skillsmart_paid as slp

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(slp.MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 1), ["212345","343456","456767","567898"])


if __name__ == '__main__':
    unittest.main()
