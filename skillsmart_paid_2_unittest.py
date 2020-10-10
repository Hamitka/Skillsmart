import unittest
import skillsmart_paid_2 as ssp2
import random

def gen_random_list_of_list(len_list: int):
    return [[random.randint(0, 1000) for i in range(n)] for n in range(len_list)]

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_lsts = gen_random_list_of_list(10)
        [self.assertEqual(ssp2.recursion_second_max(test), ssp2.second_max(test)) for test in test_lsts]
        test_lsts2 = gen_random_list_of_list(10)
        for test2 in test_lsts2:
            self.assertEqual(ssp2.recursion_second_max(test2), ssp2.second_max(test2))

    def test_something2(self):
        test_lst = [1, 2, 3]
        self.assertEqual(ssp2.recursion_second_max(test_lst), ssp2.second_max(test_lst))


if __name__ == '__main__':
    unittest.main()
