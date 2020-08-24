"""5. Задания
5.1. Разделите видимость полей и методов в каком-нибудь классе вашей программы. Сделайте все поля приватными, и напишите методы работы с ними.
5.2. Постройте небольшую иерархию классов в вашей программе. """

# попробуем нарисовать мини скелет будущей программы мониторинга IP устройств
class device:
    def __init__(self, name, vendor='', type='unknown', model=''):
        self.__name = name
        self.__vendor = vendor
        self.__type = type
        self.__model = model

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_vendor(self):
        return self.__vendor
    def set_vendor(self, v):
        self.__vendor = v
    def get_type(self):
        return self.__type


class IP_device(device):
    # а иной способ добавления атрибутов к атрибутам класса-родителя есть?
    # а то этот как то "режет" взгляд
    def __init__(self, name, ip_address, vendor='', type='', model=''):
        super().__init__(name, vendor, type, model)
        self.__ip_address = ip_address

    def get_ip_address(self):
        return self.__ip_address
    def set_ip_address(self, ip_address):
        self.__ip_address = ip_address


class IP_not_device(device):
    #здесь пока не придумал конкретные методы
    pass

class router(IP_device):
    def set_type(self):
        self.__type = 'router'

class switch(IP_device):
    def set_type(self):
        self.__type = 'switch'


class wireless(IP_device):
    def set_type(self):
        self.__type = 'wireless'


device1 = IP_device('some_device1', '10.0.0.1')
device2 = IP_not_device('some_device_wo_IP')
device3 = router('router1', '10.0.0.3')

print(device1.get_name(), device1.get_ip_address(), device1.get_type())
print(device2.get_name(), device2.get_type())
print(device3.get_name(), device3.get_ip_address(), device3.get_type())

device3.set_type()

#здесь я не понял, почему тип устройства не поменялся, метод set_type в подклассе router не верный?
print(device3.get_name(), device3.get_ip_address(), device3.get_type())