# Задание 4 . Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл (или вывести в терминал) многочлен степени k.
#Пример:
#- k = 2  => 2*x² + 4*x + 5
#- k = 3  => 41*x^3 + 6*x² + 2*x + 98


from random import randint

k = int(input('Введите K: '))
for i in range(k, 0, -1):
    factor = randint(1, 101)
    if factor == 0:
        continue
    elif factor == 1:
        factor = ''
    else: 
        factor = f'{factor}*x**{i} +' if i != 1 else f'{factor}*x +'
    print(factor, end=' ')
print(f'{randint(1, 101)} = 0')

