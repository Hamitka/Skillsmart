import socket

# создаем объект типа socket, сетевой, датаграмм (т.е. по умолчанию с негарантиованной доставкой:
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Привязываем созданный объект к локальному IP, порт такой то:
sock.bind(('localhost', 12345))
# пока пустой список клиентов:
client = []
print('Start Server')
while True:
    # Кортеж из данных и адреса (IP, порт) исходя из полученного сообщения (размер не более 1024 Байт):
    data, addres = sock.recvfrom(1024)
    # Вывод в консоль IP и порт клиента, от которого принято сообщение:
    print(addres[0], addres[1])
    # Если клиент не в списке, добавить в список:
    if addres not in client:
        client.append(addres)
    for clients in client:
        # шлем сообщение всем клиентам, кроме клиента отправителя:
        if clients == addres:
            continue
        sock.sendto(data, clients)
