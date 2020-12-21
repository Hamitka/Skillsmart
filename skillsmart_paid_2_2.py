import socket
import threading


def read_sok():
    """определяем функцию принимающую некие данные
    размером не более 1024 Байт"""
    while True:
        data = sor.recv(1024)
        print(data.decode('utf-8'))

# задаем кортеж из IP, порт сервера
server = 'localhost', 12345
# задаем свой иентификтор (ник)
alias = input()
# создаем объект типа socket, сетевой, датаграмм (т.е. по умолчанию с негарантиованной доставкой:
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Привзяывем объект к динамическому (свободному) порту
sor.bind(('', 0))
# шлем на сервер для broadcast информациооное сообщение о присоединении к чату:
sor.sendto((alias + ' Connect to server').encode('utf-8'), server)
# создаем поток из созданной функции по приему сообщений
potok = threading.Thread(target=read_sok)
potok.start()
# и, сосбвтенно, сам "чат", обем сообщениями с клиентами через сервер
while True:
    mensahe = input()
    sor.sendto(('[' + alias + ']' + mensahe).encode('utf-8'), server)
