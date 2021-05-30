import unittest
import DynArray as da


class MyTestCase(unittest.TestCase):
    def test_dyn_array_append(self):
        i_start = 16
        dyn_array = da.DynArray()
        [dyn_array.append(i) for i in range(i_start)]
        list_pattern = [i for i in range(i_start)]
        self.assertEqual(list_pattern, list(dyn_array))
        self.assertEqual(16, dyn_array.capacity)

        item_add = 88
        dyn_array.append(item_add)
        list_pattern.append(item_add)
        self.assertEqual(list_pattern, list(dyn_array))
        self.assertEqual(32, dyn_array.capacity)

    def test_dyn_array_insert(self):
        i_start = 15
        dyn_array = da.DynArray()
        [dyn_array.append(i) for i in range(i_start)]
        list_pattern = [i for i in range(i_start)]
        self.assertEqual(list_pattern, list(dyn_array))
        self.assertEqual(16, dyn_array.capacity)

        # insert into end:
        item_add = i_start
        dyn_array.insert(i_start, item_add)
        list_pattern.append(item_add)
        self.assertEqual(list_pattern, list(dyn_array))

        # insert into middle:
        i_insert, item_add = 4, 3.5
        dyn_array.insert(i_insert, item_add)
        list_pattern.insert(i_insert, item_add)
        self.assertEqual(list_pattern, list(dyn_array))
        self.assertEqual(32, dyn_array.capacity)

        i_insert, item_add = 1, 1.5
        dyn_array.insert(i_insert, item_add)
        list_pattern.insert(i_insert, item_add)
        # print(list_pattern, list(dyn_array), sep='\n')
        self.assertEqual(list_pattern, list(dyn_array))

        # insert into begin:
        i_insert, item_add = 0, -1
        dyn_array.insert(i_insert, item_add)
        list_pattern.insert(i_insert, item_add)
        # print(list_pattern, list(dyn_array), sep='\n')
        self.assertEqual(list_pattern, list(dyn_array))

        # insert into unallowable index:
        self.assertRaises(IndexError, dyn_array.insert, -1, 2)
        self.assertRaises(IndexError, dyn_array.insert, 100, 100)

    def test_dyn_array_delete(self):
        i_start = 33
        dyn_array = da.DynArray()
        [dyn_array.append(i) for i in range(i_start)]
        list_pattern = [i for i in range(i_start)]
        self.assertEqual(list_pattern, list(dyn_array))

        # del from end
        dyn_array.delete(i_start - 1)
        del list_pattern[i_start - 1]
        self.assertEqual(list_pattern, list(dyn_array))

        # del from begin
        dyn_array.delete(0)
        del list_pattern[0]
        self.assertEqual(list_pattern, list(dyn_array))

        # del from middle
        dyn_array.delete(5)
        del list_pattern[5]
        self.assertEqual(list_pattern, list(dyn_array))

        # del all and resize
        for i in range(int(len(dyn_array))):
            dyn_array.delete(0)
            del list_pattern[0]
            self.assertEqual(list_pattern, list(dyn_array))

            # del from unallowable index:
            self.assertRaises(IndexError, dyn_array.delete, -1)
            self.assertRaises(IndexError, dyn_array.delete, 100)


if __name__ == '__main__':
    unittest.main()
