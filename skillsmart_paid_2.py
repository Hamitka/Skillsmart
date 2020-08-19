"""1. Выберите две-три программы, которыми вы часто пользуетесь или с которыми играете, и подумайте, какие в них могут быть классы/объекты, придуманные разработчиками?
 Опишите своими словами, что это могут быть за классы, и какова их структура. """
"""ну возьмем самое частое мое в использовании ПО - web browser
предполагаю, что есть некий класс вкладок"""
class tab():
    tab_name = 'get from html'
    tab_num = 1
    tab_url = ''
    tab_http = 'https:\\'
#класс закладок
class favorites():
    path = 'top'
    url = ''
    name = ''

"""ну и для простоты возьмем любую игру
в ней наверняка есть некие классы персонажей, рас, амуниций, артефактов, заданий и прочее"""
class pers():
    name = ''
    gender = 'male'
    age = '18'
class sword():
    material = 'steel'
    lenght = 60
    type = 'two-handed'
    weigth = 10

"""2. Сделайте два простых класса из любой компьютерной темы, которая вам интересна. 
Создайте несколько объектов этих классов, поприсваивайте значения их полям, выведите их на экран. """
class device():
    vendor = 'huawei'
    type = 'router'
    model = 'NE40'
    version = ''

class interface():
    type = 'GigabitEthetnet'
    sub = 0 #vlan
    encapsulation = 'dot1q'
    description = ''
    int_type = 'L3'
    rate_limit_in = 0
    rate_limit_out = 0

router1 = device()
router2 = device()
router2.vendor = 'cisco'
router2.model = 'ASR9006'

interface1 = interface()
interface1.sub = 455
interface1.int_type = 'L2'
interface2 = interface()
interface2.sub = 2094
interface2.description = 'for_test'

interface3 = interface2

print(router1.vendor, router1.model, router1.type)
print(router2.vendor, router2.model, router2.type)

print('interface1: ', interface1.type, interface1.description, interface1.sub, interface1.int_type)
print('interface2: ', interface2.type, interface2.description, interface2.sub, interface2.int_type)
print('interface3: ', interface3.type, interface3.description, interface3.sub, interface2.int_type)

"""3. Напишите наглядный пример, который демонстрирует побочный эффект от передачи объектов по ссылке. """
interface3.sub = 333
print('побочный эффект после interface3.sub = 333')
print('interface2: ', interface2.type, interface2.description, interface2.sub, interface2.int_type)
print('interface3: ', interface3.type, interface3.description, interface3.sub, interface2.int_type)
print('воочую убеждаемся, что переменные ссылаются на объекты, изменение одной переменной приводит к изменению самого объекта, а значит и всех переменых, ссылающихся на этот объект')


#output:
huawei NE40 router
cisco ASR9006 router
interface1:  GigabitEthetnet  455 L2
interface2:  GigabitEthetnet for_test 2094 L3
interface3:  GigabitEthetnet for_test 2094 L3
побочный эффект после interface3.sub = 333
interface2:  GigabitEthetnet for_test 333 L3
interface3:  GigabitEthetnet for_test 333 L3
воочую убеждаемся, что переменные ссылаются на объекты, изменение одной переменной приводит к изменению самого объекта, а значит и всех переменых, ссылающихся на этот объект

Process finished with exit code 0
