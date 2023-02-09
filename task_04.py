# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random 

print('Напишите степень ')
deg = int(input())
numbers = []
randomNumber = random.randint(1,3)
if(randomNumber == 1):
    polynomial = f'{random.randint(1, 100)} * x^{deg} = 0'
if(randomNumber == 2):
    polynomial = f'{random.randint(1, 100)} * x^{deg} + {random.randint(1, 100)} * x  + {random.randint(1, 100)} = 0'
if(randomNumber == 3):
    polynomial = f'{random.randint(1, 100)} * x^{deg} + {random.randint(1, 100)} * x^{deg - 1}  + x x^{-deg}= 0'
file = open("Polynomial.txt", "w")
file.write(polynomial)
file.close
