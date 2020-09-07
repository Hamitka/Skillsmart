"""4. Задание
Напишите функцию поиска подстроки в строке (на основе вашего решения выпускной задачи начального курса) и четыре вида тестов для неё. """

import unittest
import skillsmart_paid_2 as slp2
import random
import string

# генератор случайных строк:
def get_random_string(length) -> string:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

class MyTestCase(unittest.TestCase):
    #в данной конкретной задаче проверку своих функций можно проверять и встроенными, к пример "in"
    def test_something1(self):
        test_string1, test_string2 = '12345', '234'
        self.assertEqual(slp2.in_string4(test_string1, test_string2), True)
        self.assertEqual(slp2.in_string3(test_string1, test_string2), (test_string2 in test_string1))
        self.assertEqual(slp2.in_string2(test_string1, test_string2), (test_string2 in test_string1))

    def test_something2(self):
        test_string1, test_string2 = '12345', '3456'
        self.assertEqual(slp2.in_string4(test_string1, test_string2), False)
        self.assertEqual(slp2.in_string3(test_string1, test_string2), (test_string2 in test_string1))
        self.assertEqual(slp2.in_string2(test_string1, test_string2), (test_string2 in test_string1))

    def test_something3(self):
        test_string1, test_string2 = '1231234', '1234'
        self.assertEqual(slp2.in_string4(test_string1, test_string2), True)
        self.assertEqual(slp2.in_string3(test_string1, test_string2), (test_string2 in test_string1))
        self.assertEqual(slp2.in_string2(test_string1, test_string2), (test_string2 in test_string1))

    def test_something4(self):
        test_string1, test_string2 = '', ''
        self.assertEqual(slp2.in_string4(test_string1, test_string2), True)
        self.assertEqual(slp2.in_string3(test_string1, test_string2), (test_string2 in test_string1))
        self.assertEqual(slp2.in_string2(test_string1, test_string2), (test_string2 in test_string1))

    def test_something5_random(self):
        for i in range(1, 100):
            string1 = get_random_string(random.randint(1, 10000))
            string2 = get_random_string(random.randint(1, 1000))
            self.assertEqual(slp2.in_string4(string1, string2), (string2 in string1))
            self.assertEqual(slp2.in_string3(string1, string2), (string2 in string1))
            self.assertEqual(slp2.in_string2(string1, string2), (string2 in string1))

    def test_something6(self):
        test_string1, test_string2 = '1234', ''
        self.assertEqual(slp2.in_string4(test_string1, test_string2), True)
        self.assertEqual(slp2.in_string3(test_string1, test_string2), (test_string2 in test_string1))
        self.assertEqual(slp2.in_string2(test_string1, test_string2), (test_string2 in test_string1))

    def test_something7(self):
        test_string1, test_string2 = '', '1234'
        self.assertEqual(slp2.in_string4(test_string1, test_string2), False)
        self.assertEqual(slp2.in_string3(test_string1, test_string2), (test_string2 in test_string1))
        self.assertEqual(slp2.in_string2(test_string1, test_string2), (test_string2 in test_string1))

    def test_something8_big(self):
        test_string1, test_string2 = get_random_string(10000000), 'xx'
        self.assertEqual(slp2.in_string4(test_string1, test_string2), (test_string2 in test_string1))
        self.assertEqual(slp2.in_string3(test_string1, test_string2), (test_string2 in test_string1))
        self.assertEqual(slp2.in_string2(test_string1, test_string2), (test_string2 in test_string1))

    def test_something9_big(self):
        test_string1, test_string2 = get_random_string(10000000), get_random_string(3)
        self.assertEqual(slp2.in_string4(test_string1, test_string2), (test_string2 in test_string1))
        self.assertEqual(slp2.in_string3(test_string1, test_string2), (test_string2 in test_string1))
        self.assertEqual(slp2.in_string2(test_string1, test_string2), (test_string2 in test_string1))
        print (test_string2 in test_string1)


if __name__ == '__main__':
    unittest.main()
