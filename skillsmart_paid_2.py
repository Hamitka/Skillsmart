"""
 5.3. Задания
5.3.1. Условимся, что в нашем демонстрационном XML-документе только два уровня вложенности (languages и pc).
Выведите на консоль содержание каждого узла как первого, так и второго уровня, включая название тега, список атрибутов и значение.
5.3.2. Пользуясь только сведениями из данного занятия, напишите функцию, которая формирует список всех значений (по всем узлам)
для конкретного тега, если задано его название (например, на вход функции подаётся "sex" или "pc_item").
5.3.3. Напишите функцию, которая возвращает количество узлов в документе, включая дочерние, оснащённые заданным атрибутом.
Прим. Наличие ключа в словаре можно проверить так (тестом наличия значения в списке ключей словаря):
значение in имя-словаря.keys()
Например:
"name" in languages[i].attrib.keys()
5.3.4. Напишите тесты к двум предыдущим заданиям.
"""

import xml.etree.ElementTree as ETree

# 5.3.1. Условимся, что в нашем демонстрационном XML-документе только два уровня вложенности (languages и pc).
# Выведите на консоль содержание каждого узла как первого, так и второго уровня, включая название тега, список атрибутов и значение.
xml1 = ETree.parse('demo.xml')
root = xml1.getroot()
for item in root:
    if not len(item):
        print(item.tag, item.attrib, item.text)
    else:
        for subitem in item:
            print(subitem.tag, subitem.attrib, subitem.text)


# тоже самое через рекурсию:
def item_print(xml_root):
    for item in xml_root:
        if not len(item):
            print(item.tag, item.attrib, item.text)
        else:
            item_print(item)


# item_print(root)


# 5.3.2. Пользуясь только сведениями из данного занятия, напишите функцию, которая формирует список всех значений (по всем узлам)
# для конкретного тега, если задано его название (например, на вход функции подаётся "sex" или "pc_item").

def get_xml_value(xml_root, xml_tag: str = None):
    xml_attrib = []

    def get_tag(xml_root):
        for item in xml_root:
            if not len(item):
                if item.tag == xml_tag:
                    xml_attrib.append(item.text)
            else:
                get_tag(item)

    if not xml_tag:
        return None
    else:
        get_tag(xml_root)
    return xml_attrib


# print(get_xml_value(root, 'pc_item'))


# 5.3.3. Напишите функцию, которая возвращает количество узлов в документе, включая дочерние, оснащённые заданным атрибутом.

def count_xml_attrib(xml_root, xml_attrib: str):
    xml_count = 0
    # через рекусрию:
    # def parse_xml_attrinb(xml_root):
    #     nonlocal xml_count
    #     for item in xml_root:
    #         if not len(item):
    #             if xml_attrib in item.attrib.keys():
    #                 xml_count += 1
    #         else:
    #             parse_xml_attrinb(item)

    if not xml_attrib:
        return 0
    else:
        for item in xml_root:
            if not len(item):
                if xml_attrib in item.attrib.keys():
                    xml_count += 1
            else:
                for subitem in item:
                    if xml_attrib in subitem.attrib.keys():
                        xml_count += 1
    return xml_count


# print(count_xml_attrib(root, 'name'))
