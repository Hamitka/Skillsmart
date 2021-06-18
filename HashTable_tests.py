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

    def test_native_dict(self):
        my_dict = ht.NativeDictionary(17)
        for i in range(my_dict.size):
            my_dict.put('key' + str(i), 'value' + str(i))
            self.assertEqual(True, my_dict.is_key('key' + str(i)))
            self.assertEqual('value' + str(i), my_dict.get('key' + str(i)))

        print([f'{my_dict.slots[i]}: {my_dict.values[i]}' for i in range(my_dict.size)])
        my_dict.put('key5', 'value555')
        print([f'{my_dict.slots[i]}: {my_dict.values[i]}' for i in range(my_dict.size)])
        self.assertEqual('value555', my_dict.get('key5'))
        self.assertEqual(None, my_dict.get('key555'))



if __name__ == '__main__':
    unittest.main()
