# Задание 3 .  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.

# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Восстановить
# Ввод: stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"


import random

def coding(text):
    if len(text) < 1:
        return ''
    count = 0
    el = text[0]
    result = ''
    for elem in text:
        if elem == elem:
            count += 1
        else:
            result += str(count) + el
            count += 1
            el = elem
    else:
        result += str(count) + el
    return result

def decoding(text: str) -> str:
    if len(text) < 1:
        return ''
    num = ''
    result = ''
    for elem in text:
        if elem.isdigit():
            num += elem
        else:
            for i in range(int(num)):
                result += elem
            else:
                num = ''
    return result

print('Кодироввание')
print(coding('aaabbbbccbbb'))
print('Раскодирование')
print(decoding('3a4b2c3b'))

            