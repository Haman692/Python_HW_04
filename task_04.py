# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random 

print('Напишите степень ')
deg = int(input())
numbers = [random.randint(0,100) for i in range(random.randint(1,3))]
if(len(numbers) == 1):
    polynomial = f'{numbers[0]} * x^{deg} = 0'
if(len(numbers) == 3):
    polynomial = f'{numbers[0]} * x^{deg} + {numbers[1]} * x  + {numbers[2]} = 0'
if(len(numbers) == 2):
    polynomial = f'{numbers[0]} * x^{deg} + {numbers[1]} * x^{deg - 1}  + x^{-deg}= 0'
file = open("Polynomial.txt", "w")
file.write(polynomial)
file.close
print(numbers)