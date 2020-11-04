import unittest
import skillsmart_paid_2 as ssp2

class MyTestCase(unittest.TestCase):
    def test_xml_value(self):
        self.assertEqual(len(ssp2.get_xml_value(ssp2.root, 'name')), 1)
        self.assertEqual(len(ssp2.get_xml_value(ssp2.root, 'age')), 1)
        self.assertEqual(len(ssp2.get_xml_value(ssp2.root, 'sex')), 1)
        self.assertEqual(len(ssp2.get_xml_value(ssp2.root, 'pc_item')), 4)
        self.assertEqual(len(ssp2.get_xml_value(ssp2.root, 'language')), 3)
        self.assertEqual(ssp2.get_xml_value(ssp2.root, 'pc_item'), ['Linux', 'Intel Core i7-8700', '64', '5000'])

    def test_count_xml_attrib(self):
        self.assertEqual(ssp2.count_xml_attrib(ssp2.root, 'name'), 7)
        self.assertEqual(ssp2.count_xml_attrib(ssp2.root, ''), 0)



if __name__ == '__main__':
    unittest.main()
