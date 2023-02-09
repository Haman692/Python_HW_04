# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math

print('Напишите число')
number = int(input())
naturalNumbers = []
dev = 2
while number > 1:
    if number%dev == 0:
        number /= dev
        naturalNumbers.append(dev) 
    else:
        dev += 1
naturalNumbers = set(naturalNumbers)
print(naturalNumbers)