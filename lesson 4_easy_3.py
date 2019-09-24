# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

random_list =[random.randint(-10, 10) for _ in range(10)]
new_list = list(i for i in random_list if (i % 3 == 0 and i > 0 and i % 4 != 0) )
print(random_list)
print(new_list)