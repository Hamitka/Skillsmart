"""
userId -- это уникальный идентификатор пользователя,
id -- уникальный идентификатор условной задачи для этого пользователя,
title -- название этой задачи,
completed -- показывает, выполнена эта задача или нет.

7. Задания
7.1. Сохраните JSON-набор, полученный через внешний API, в файл.
7.2. Посчитайте количество уникальных пользователей в этом наборе.
7.3. Посчитайте для каждого пользователя, сколько у него оригинальных задач, и сколько из них выполнено.
"""

import json
import requests

with open("file.json", "w") as json_file:
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    json_file.write(response.text)

with open("file.json", "r") as json_file:
    result = json.load(json_file)

users = {}
for i in range(len(result)):
    users.setdefault(result[i]["userId"], {"num": 0, "completed": 0})
    users[result[i]["userId"]]["num"] += 1
    if result[i]["completed"] == True:
        users[result[i]["userId"]]["completed"] += 1

print('Количество всех пользоваталей %d' % (len(users.keys())))
[print('Количество завершеных задач у пользователя %d равно %d из %d' % (i, users[i]["completed"], users[i]["num"])) for i in users.keys()]
