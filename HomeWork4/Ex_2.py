# Задание 2 . Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# 24     
# 2 2 2 3


num = int(input("Введите число N: "))
i = 2
list = []
while i <= num:
    if num % i == 0:
        list.append(i)
        num //= i
    else:
        i += 1
print(f"Простые множители равны: {list}") 


    