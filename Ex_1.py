# Задание 1 . Вычислить число Pi c заданной точностью d, не используя ф. round()
# Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
num = int(input())
stroka = str(pi)
print(float (stroka[0:num+2]))

