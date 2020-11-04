import unittest
import skillsmart_paid_2 as ssp2
import random

def gen_random_list_of_list(len_list: int):
    return [[random.randint(0, 1000) for i in range(n)] for n in range(2, len_list)]

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_lsts = gen_random_list_of_list(10)
        [self.assertEqual(ssp2.second_max(test), sorted(test)[-2]) for test in test_lsts]
        test_lsts2 = gen_random_list_of_list(10)
        for test2 in test_lsts2:
            self.assertEqual(ssp2.second_max(test2), sorted(test2)[-2])

    def test_something2(self):
        test_lst = [1, 2, 3]
        self.assertEqual(ssp2.second_max(test_lst), sorted(test_lst)[-2])


if __name__ == '__main__':
    unittest.main()
