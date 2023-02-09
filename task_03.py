# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


print('Введите набор чисел')
numbers = str(input())
numberList = [int(i) for i in numbers]
newDict = {}
newList = []
for i in numberList:
    newDict[i] = newDict.get(i, 0) + 1
    if newDict.get(i) == 1:
        newList.append(i)
print(newList)

