# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4
x = int(input("Введите число больше 0 и меньше 10 "))
while 0 > x or x > 10:
    x = int(input("Нет. Еще раз повторяю: число должно быть больше 0 и меньше 10 "))
else:
    y = x ** 2
    print(y)
