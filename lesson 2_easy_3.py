## Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numbers = [2,3,7,15,68,13,54,86,43]
new_numbers = []
for element in numbers:
    if element % 2 == 0:
        element = float (element / 4)
        new_numbers.append(element)
    elif element % 2 == 1:
        element = float (element * 2)
        new_numbers.append(element)
print (new_numbers)