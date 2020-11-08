import unittest
import skillsmart_paid_2 as ssp2

class MyTestCase(unittest.TestCase):
    ## 6.6.1. Напишите функцию, которая формирует список всех узлов по заданному тегу независимо от их глубины в XML-документе.
    # На вход функция получает корневой узел.
    def test_xml_list_node(self):
        self.assertEqual(len(ssp2.get_xml_node(ssp2.root, 'sex')), 1)
        self.assertEqual(len(ssp2.get_xml_node(ssp2.root, 'languages')), 1)
        self.assertEqual(len(ssp2.get_xml_node(ssp2.root, 'language')), 3)
        self.assertEqual(len(ssp2.get_xml_node(ssp2.root, 'pc')), 1)
        self.assertEqual(len(ssp2.get_xml_node(ssp2.root, 'pc_item')), 4)

    #6.6.2. Напишите функцию, которая находит родителя заданного узла.
    def test_xml_parrent(self):
        self.assertEqual(ssp2.get_xml_parent(ssp2.root, 'sex').tag, 'data')
        self.assertEqual(ssp2.get_xml_parent(ssp2.root, 'languages').tag, 'data')
        self.assertEqual(ssp2.get_xml_parent(ssp2.root, 'language').tag, 'languages')
        self.assertEqual(ssp2.get_xml_parent(ssp2.root, 'pc').tag, 'data')
        self.assertEqual(ssp2.get_xml_parent(ssp2.root, 'pc_item').tag, 'pc')
        self.assertEqual(ssp2.get_xml_parent(ssp2.root, ''), None)
        self.assertEqual(ssp2.get_xml_parent(ssp2.root, 'blabla'), None)


    # 6.6.3. Напишите функцию, которая удаляет все узлы по заданному тегу независимо от их глубины в XML-документе.
    def test_xml_del_node(self):
        tag1 = 'sex'
        self.assertEqual(len(ssp2.root.findall(tag1)), 1)
        ssp2.del_xml_node(ssp2.root, tag1)
        self.assertEqual(len(ssp2.root.findall(tag1)), 0)
        tag2 = 'language'
        for sub in ssp2.root.iter('languages'):
            self.assertEqual(len(sub.findall(tag2)), 3)
        ssp2.del_xml_node(ssp2.root, tag2)
        for sub in ssp2.root.iter('languages'):
            self.assertEqual(len(sub.findall(tag2)), 0)


if __name__ == '__main__':
    unittest.main()
