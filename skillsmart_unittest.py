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
        self.assertEqual(slp2.in_string4('12345', '234'), True)
        self.assertEqual(slp2.in_string3('12345', '234'), ('234' in '1234'))
        self.assertEqual(slp2.in_string2('12345', '234'), ('234' in '1234'))

    def test_something2(self):
        self.assertEqual(slp2.in_string4('12345', '3456'), False)
        self.assertEqual(slp2.in_string3('12345', '3456'), ('3456' in '1234'))
        self.assertEqual(slp2.in_string2('12345', '3456'), ('3456' in '1234'))

    def test_something3(self):
        self.assertEqual(slp2.in_string4('1231234', '1234'), True)
        self.assertEqual(slp2.in_string3('1231234', '1234'), ('1234' in '1231234'))
        self.assertEqual(slp2.in_string2('1231234', '1234'), ('1234' in '1231234'))

    def test_something4(self):
        self.assertEqual(slp2.in_string4('1231234', '1234'), True)
        self.assertEqual(slp2.in_string3('1231234', '1234'), ('1234' in '1231234'))
        self.assertEqual(slp2.in_string2('1231234', '1234'), ('1234' in '1231234'))

    def test_something5_random(self):
        for i in range(1, 10000):
            string1 = get_random_string(random.randint(1, 1000))
            string2 = get_random_string(random.randint(1, 1000))
            self.assertEqual(slp2.in_string4(string1, string2), (string2 in string1))
            self.assertEqual(slp2.in_string3(string1, string2), (string2 in string1))
            self.assertEqual(slp2.in_string2(string1, string2), (string2 in string1))

if __name__ == '__main__':
    unittest.main()
