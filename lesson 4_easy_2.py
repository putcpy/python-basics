
# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

a = ["apple", "apricot", "melon", "orange"]
b = ["orange", "lime", "peach","apricot"]
all_fruits = [item for item in a if item in b]
print (all_fruits)

