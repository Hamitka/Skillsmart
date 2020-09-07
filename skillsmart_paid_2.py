"""напишите функцию с двумя параметрами-строками. Функция возвращает булево значение,
True если вторая строка содержится в первой строке как подстрока, и False в противном случае.
Например,
f("12345", "234") = True
f("12345", "235") = False
Для решения стандартные возможности типа s1 in s2 использовать нельзя, только условиями и циклами."""

def in_string4(string1: str, string2: str):
    len_str1, len_str2 = len(string1), len(string2)
    if len_str2 > len_str1:
        return False
    elif string1 == string2:
        return True
    elif string2 == '':
        return True
    elif string1 == '':
        return False
    k = 0
    for i in range(len_str1):
        if string1[i] == string2[k]:
            k+=1
        elif string1[i] == string2[0]:
            k=1
        else:
            k=0
        if k == len_str2:
            return True
    return False

def in_string3(string1: str, string2: str):
    len_str1, len_str2 = len(string1), len(string2)
    if len_str2 > len_str1:
        return False
    elif string1 == string2:
        return True
    elif string2 == '':
        return True
    elif string1 == '':
        return False
    for i in range(len_str1 - len_str2 + 1):
        for j in range(len_str2):
            if string1[i + j] != string2[j]:
                break
            if j == len_str2 - 1:
                return True
    return False


def in_string2(string1: str, string2: str):
    len_str1, len_str2 = len(string1), len(string2)
    if len_str2 > len_str1:
        return False
    elif string1 == string2:
        return True
    i = j = 0
    while i < len_str1 and j < len_str2:
        if string1[i] != string2[j]:
            if j > 0: i -= 1
            j = 0
        else:
            j += 1
        i += 1
    if j == len_str2:
        return True
    return False


def in_string(string1: str, string2: str):
    len_str1, len_str2 = len(string1), len(string2)
    if len_str2 > len_str1:
        return False
    for i in range(len_str1):
        if string1[i:i + len_str2] == string2:
            return True
    return False


# print(in_string('12345', '234'))
# print(in_string2('12345', '234'))
# print(in_string3('12345', '234'))
# print(in_string4('12345', '234'))
# print('------')
# print(in_string('1234511111111111', '1111'))
# print(in_string2('1234511111111111', '1111'))
# print(in_string3('1234511111111111', '1111'))
# print(in_string4('1234511111111111', '1111'))
# print('------')
# print(in_string('12345', '2345'))
# print(in_string2('12345', '2345'))
# print(in_string3('12345', '2345'))
# print(in_string4('12345', '2345'))
# print('------')
# print(in_string('12345', '235'))
# print(in_string2('12345', '235'))
# print(in_string3('12345', '235'))
# print(in_string4('12345', '235'))
# print('------')
# print(in_string('345', '12345'))
# print(in_string2('345', '12345'))
# print(in_string3('345', '12345'))
# print(in_string4('345', '12345'))
# print('------')
# print(in_string('345678', '56789'))
# print(in_string2('345678', '56789'))
# print(in_string3('345678', '56789'))
# print(in_string4('345678', '56789'))
# print('------')
# print(in_string('допдопа', 'допа'))
# print(in_string2('допдопа', 'допа'))
# print(in_string3('допдопа', 'допа'))
# print(in_string4('допдопа', 'допа'))
