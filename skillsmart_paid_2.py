""" 6.6. Задания
6.6.1. Напишите функцию, которая формирует список всех узлов по заданному тегу независимо от их глубины в XML-документе.
На вход функция получает корневой узел.
6.6.2. Напишите функцию, которая находит родителя заданного узла.
6.6.3. Напишите функцию, которая удаляет все узлы по заданному тегу независимо от их глубины в XML-документе.
6.6.4. Для трёх предыдущих функций напишите тесты.
"""

import xml.etree.ElementTree as ETree

xml1 = ETree.parse('demo.xml')
root = xml1.getroot()


# 6.6.1. Напишите функцию, которая формирует список всех узлов по заданному тегу независимо от их глубины в XML-документе.
# На вход функция получает корневой узел.

# через .iter
def get_xml_node(xml_root, xml_tag: str):
    xml_nodes = []
    for item in xml_root.iter():
        if item.tag == xml_tag:
            xml_nodes += [item]
    return xml_nodes


# через рекурсию
def get_xml_node_rec(xml_root, xml_tag: str):
    xml_nodes = []

    def get_tag(xml_root):
        for item in xml_root:
            if not len(item):
                if item.tag == xml_tag:
                    xml_nodes.append(item)
            else:
                get_tag(item)

    get_tag(xml_root)
    return xml_nodes


# 6.6.2. Напишите функцию, которая находит родителя заданного узла.
def get_xml_parent(xml_root, xml_tag: str):
    for item in xml_root.iter():
        if item.find(xml_tag) is not None:
            return item
    return None


# 6.6.3. Напишите функцию, которая удаляет все узлы по заданному тегу независимо от их глубины в XML-документе.
def del_xml_node(xml_root, xml_tag: str):
    for item in xml_root.iter():
        subitems = item.findall(xml_tag)
        for i in subitems:
            item.remove(i)
    return xml_root

