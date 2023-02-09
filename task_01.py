# Вычислить число c заданной точностью d
import sys
import math
print('Подсчет длинны круга, по радиусу')
print('Введите радиус окружности')
radius = int(input())
print('введите точность')
d = float(input())
i = float
if d >= 1:
    sys.exit('Число должнобуть по примеру: 0.001')
else:
    lenghtFloat = len(str(d))
    i = 2*math.pi*radius
    print(round(i, lenghtFloat - 2))
    