import unittest
import skillsmart_paid_2 as ssp2


class MyTestCase(unittest.TestCase):
    # 1. Самостоятельно разберитесь, как сделать из класса List2 итератор с конструктором,
    # чтобы он работал не только начиная с 1, а с любого заданного значения:
    def test_List2(self):
        n = 10
        test_lst2 = ssp2.List2(n)
        itest_lst2 = iter(test_lst2)
        for i in range(9):
            self.assertEqual(next(itest_lst2), n * (2 ** i))


if __name__ == '__main__':
    unittest.main()
