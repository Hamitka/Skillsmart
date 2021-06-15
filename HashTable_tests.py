import unittest
import HashTable as ht


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_hash_table = ht.HashTable(17, 3)
        my_hash_table.put('test')
        my_hash_table.put('test')
        my_hash_table.put('test')
        my_hash_table.put('test')
        my_hash_table.put('test')
        my_hash_table.put('test1')
        my_hash_table.put('test1')
        my_hash_table.put('test1')
        my_hash_table.put('test1')
        my_hash_table.put('test1')
        my_hash_table.put('test2')
        my_hash_table.put('test2')
        my_hash_table.put('test2')
        my_hash_table.put('test2')
        my_hash_table.put('test2')
        print(my_hash_table.slots)

        print(my_hash_table.find('test'))


if __name__ == '__main__':
    unittest.main()
