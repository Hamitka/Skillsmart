"""напишите функцию с двумя параметрами-строками. Функция возвращает булево значение,
True если вторая строка содержится в первой строке как подстрока, и False в противном случае.
Например,
f("12345", "234") = True
f("12345", "235") = False
Для решения стандартные возможности типа s1 in s2 использовать нельзя, только условиями и циклами."""

def in_string(string1:str, string2:str):
    len_str1, len_str2 = len(string1), len(string2)
    if len_str2 > len_str1:
        return False
    for i in range(len_str1):
        if string1[i:i+len_str2] == string2:
            return True
    return False


print(in_string('12345', '234'))
print(in_string('12345', '2345'))
print(in_string('12345', '235'))
print(in_string('345', '12345'))