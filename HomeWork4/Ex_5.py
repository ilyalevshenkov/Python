# Задание 5 . Дополнительное Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
#Файл1: 2*x² + 4*x + 5
# Файл2: 41*x^3 + 6*x² + 2*x + 98
# Вывод Файл3: 41*x^3 + 8*x^2 + 6*x + 103

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import re
import pathlib
import logging

def ExponentUnification(polinomial_sting):
    return polinomial_sting.replace('ВІ','^2') # все-таки chr(178) или строка 'BI' ?!

def ConcatenateDict(result_dict):
    result_polinomial = []
    for k,v in result_dict.items():
        result_polinomial.append(f'{v}*{k}') if k != '1' else result_polinomial.append(f'{v}') # тернарный оператор    
    return ' + '.join(result_polinomial)

def ParsePolinome(polinomial):
    polinomial_dict = {}
    monomials = re.split(r'[+-]',polinomial)
    for monomial in monomials:
        monomial_parts = [p.strip() for p in monomial.split('*', 1)]
        if len(monomial_parts) == 1:
            monomial_parts.append('1')
        polinomial_dict[monomial_parts[1]] = int(monomial_parts[0])
    return polinomial_dict

def MergePolinomes(polinomial1_dict,polinomial2_dict):
    for item in polinomial2_dict:
        if item in polinomial1_dict:
            polinomial2_dict[item] += polinomial1_dict[item]
    for item in polinomial1_dict:
        if item not in polinomial2_dict:
            polinomial2_dict[item] = polinomial1_dict[item]
    return polinomial2_dict

files = [pathlib.Path(f'file{i}.txt') for i in range(3)] # ПРАВИЛЬНО РАБОТАЕТ ТОЛЬКО ЧЕРЕЗ СПЕЦИАЛЬНО ОТКРЫТЫЙ ТЕРМИНАЛ В VS CODE (Open in Integrated Terminal)

try:
    with open(files[0]) as file0,\
    open(files[1]) as file1,\
    open(files[2],'w') as file2: # создаст файл
        polinomial1_dict = ParsePolinome(ExponentUnification(file0.readline()))
        polinomial2_dict = ParsePolinome(ExponentUnification(file1.readline()))
        result_dict = MergePolinomes(polinomial1_dict,polinomial2_dict)
        file2.write(ConcatenateDict(result_dict))
        # file2.write(f'{file0.readline()} + {file1.readline()}') если бы не надо было сокращать...
except OSError as error:
    logging.error('Editing file %s failed due to: %s', files[2], error)