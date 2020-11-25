import unittest
import skillsmart_paid_2 as ssp2


class MyTestCase(unittest.TestCase):
    # 1. Самостоятельно разберитесь, как сделать из класса List2 итератор с конструктором,
    # чтобы он работал не только начиная с 1, а с любого заданного значения:
    def test_List2(self):
        n = 10
        test_lst2 = ssp2.List2(n)
        itest_lst2 = iter(test_lst2)
        for i in range(n):
            self.assertEqual(next(itest_lst2), n * (2 ** i))

    def test_List2v2_not_infinity(self):
        n = 10
        m = 10
        test_lst2 = ssp2.List2v2(n, m)
        itest_lst2 = iter(test_lst2)
        for i in range(m):
            temp = next(itest_lst2)
            self.assertEqual(temp, n * (2 ** i))
        self.assertRaises(StopIteration, next, itest_lst2)

    def test_List2v2_infinity(self):
        n = 10
        m = 3
        test_lst2 = ssp2.List2v2(n, m, True)
        itest_lst2 = iter(test_lst2)
        for i in range(m):
            temp = next(itest_lst2)
            self.assertEqual(temp, n * (2 ** i))
        self.assertEqual(next(itest_lst2), 10)
        self.assertEqual(next(itest_lst2), 20)
        self.assertEqual(next(itest_lst2), 40)
        self.assertEqual(next(itest_lst2), 10)
        self.assertEqual(next(itest_lst2), 20)
        self.assertEqual(next(itest_lst2), 40)


if __name__ == '__main__':
    unittest.main()
