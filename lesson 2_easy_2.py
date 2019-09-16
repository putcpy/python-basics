
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

protein = ['beef', 'chicken', 'lamb', 'veal', 'duck', 'turkey']
poultry = ['chicken', 'turkey', 'duck', 'swan']
various_meat = set(protein + poultry)
print (various_meat)