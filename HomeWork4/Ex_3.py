# Задание 3 . Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.(Вывод тех элементов, которые были без повторов)
# Ввод: 1 2 3 2 4 4
# Вывод: 1 3



spisok = [int(i) for i in input('Введите числа через пробел: ').split()]
result = []
for i in spisok:
    if spisok.count(i) ==1:
        result.append(i)
print('Неповторяющиеся числа последовательности:  ')
print(result)

