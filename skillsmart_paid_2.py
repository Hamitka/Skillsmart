""" Задание
Дополните два класса, которые вы спроектировали в предыдущем задании, методами, подходящими для логики работы с ними. """
class device:
    def __init__(self, vendor, type, model, version):
        self.vendor = vendor
        self.type = type
        self.model = model
        self.version = version

    def upgrade(self, new_version):
        self.version = new_version

    def swap(self, new_vendor, new_model, new_version):
        self.vendor = new_vendor
        self.model = new_model
        self.version = new_version

#вот тут я не очень удачно выбрал пример, потому как у объекта данного класса предполагается изменение самих атрибутов
class interface:
    def __init__(self, int_type, type = 'GigabitEthernet', sub=None, encapsulation='dot1q', description='', ip_address = None, rate_limit=0):
        self.type = type
        self.int_type = int_type
        self.sub = sub
        self.encapsulation = encapsulation
        self.description = description
        self.ip_address = ip_address
        self.rate_limit = rate_limit

    def create_config(self):
        print('interface ' + self.type + '.' + str(self.sub))
        print('vlan-type ' + self.encapsulation + ' ' + str(self.sub))
        print('description' + self.description)
        print('ip address '+ str(self.ip_address))
        print('qos car cir ' + str(self.rate_limit) + ' inbound')
        print('qos car cir ' + str(self.rate_limit) + ' outbound')

    def delete(self):
        self.type = ''
        self.int_type = ''
        self.sub = None
        self.encapsulation = ''
        self.description = ''
        self.ip_address = None
        self.rate_limit = 0

interface1 = interface('L3', description='some_test_service', sub=300, ip_address='10.0.0.1 30', rate_limit=10000)
interface1.create_config()
interface1.delete()
interface1.create_config()