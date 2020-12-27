import socket

# создаем объект типа socket, сетевой, датаграмм (т.е. по умолчанию с негарантиованной доставкой:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Привязываем созданный объект к локальному IP, порт такой то:
sock.bind(('localhost', 12345))
sock.listen(10)
# пока пустой список клиентов:
client = []
print('Start Server')
while True:
    # Кортеж из данных и адреса (IP, порт) исходя из полученного сообщения (размер не более 1024 Байт):
    connection, address = sock.accept()
    data = connection.recv(1024)
    # Вывод в консоль IP и порт клиента, от которого принято сообщение:
    print(address[0], address[1])
    # Если клиент не в списке, добавить в список:
    if address not in client:
        client.append(address)
    for clients in client:
        # шлем сообщение всем клиентам, кроме клиента отправителя:
        if clients == address:
            continue
        connection.sendto(data, clients)