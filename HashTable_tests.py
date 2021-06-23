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

    def test_power_set(self):
        my_set = ht.PowerSet()
        my_set.put(1)
        my_set.put(3)
        my_set.put(2)
        my_set.put(6)
        my_set.put(5)
        self.assertEqual(5, my_set.size())
        self.assertEqual([1, 2, 3, 5, 6], my_set.values)
        my_set.put(5)
        self.assertEqual([1, 2, 3, 5, 6], my_set.values)
        my_set_2 = ht.PowerSet()
        for i in range(5):
            my_set_2.put(i)
        self.assertEqual(False, my_set.issubset(my_set_2))
        my_set.put(0)
        my_set.put(4)
        self.assertEqual(True, my_set.issubset(my_set_2))
        self.assertEqual(False, my_set_2.issubset(my_set))

        my_set.remove(0)
        self.assertEqual([1, 2, 3, 4, 5, 6], my_set.values)
        self.assertEqual([1, 2, 3, 4], my_set.intersection(my_set_2).values)
        my_set_3 = ht.PowerSet()
        my_set_3.put(10)
        my_set_3.put(11)
        self.assertEqual([], my_set.intersection(my_set_3).values)
        self.assertEqual([1, 2, 3, 4, 5, 6, 10, 11], my_set.union(my_set_3).values)
        my_set_4 = ht.PowerSet()
        self.assertEqual([1, 2, 3, 4, 5, 6], my_set.union(my_set_4).values)

        my_set_5 = ht.PowerSet()
        for i in range(25000):
            my_set_5.put(i)

        for i in range(10000, 15000):
            my_set_5.remove(i)
        print(my_set_5.size())

    def test_bloom_filter(self):
        my_bloom_filter = ht.BloomFilter(32)
        some_string = '0123456789'
        # my_bloom_filter.add(some_string)
        # print(my_bloom_filter.is_value('some_string'))
        print(my_bloom_filter.__bitarray__)
        for i in range(len(some_string)):
            str_rotate = some_string[i::] + some_string[:i:]
            print(str_rotate, my_bloom_filter.is_value(str_rotate))
            my_bloom_filter.add(str_rotate)
        print(my_bloom_filter.__bitarray__)
        for i in range(len(some_string)):
            str_rotate = some_string[i::] + some_string[:i:]
            print(str_rotate, my_bloom_filter.is_value(str_rotate))

    def test_native_cache(self):
        my_native_cache = ht.NativeCache(17)
        for i in range(71):
            my_native_cache.put('key' + str(i), 'val' + str(i))
        my_native_cache.get('key1')
        my_native_cache.get('key1')
        my_native_cache.get('key2')
        my_native_cache.get('key3')
        my_native_cache.put('key17', 'val17')
        my_native_cache.get('key17')
        my_native_cache.put('key18', 'val18')

        print(my_native_cache.slots)
        print(my_native_cache.values)
        print(my_native_cache.hits)


if __name__ == '__main__':
    unittest.main()
