# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа, 
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86 
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
# случайная карточка. 
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
	
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71   
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87      
#       16 49    55 77    88    
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать 
# модуль random: http://docs.python.org/3/library/random.html
# """

import random


def card_generator():
    card_massive = [random.randint(1,90) for x in range(15)]
    first_str = card_massive[0:5]
    first_str.sort()
    
    second_str = card_massive[5:10]
    second_str.sort()
    
    third_str = card_massive[10:15]
    third_str.sort()
    
    card_set = set(card_massive)
    
    while len(card_set)<15:
        card_set.add (random.randint(1,90))
    card_massive = list(card_set)
    
    while len(first_str)<9:
        l = len(first_str)
        first_str.insert(random.randint(0,l),"")
        
    while len(second_str)<9:
        l = len(second_str)
        second_str.insert(random.randint(0,l),"")
        
    while len(third_str)<9:
        l = len(third_str)
        third_str.insert(random.randint(0,l),"")
    
    return first_str, second_str, third_str

def print_card(first_str, second_str, third_str):
    format_first_str = ['{:2}'.format(num) for num in first_str]
    format_second_str = ['{:2}'.format(num) for num in second_str]
    format_third_str = ['{:2}'.format(num) for num in third_str]
        
    print ("--------------------------")
    print (' '.join(format_first_str))
    print (' '.join(format_second_str))
    print (' '.join(format_third_str))
    print ("--------------------------")
    
print ("Ваша карточка")
player1_first_str, player1_second_str, player1_third_str = card_generator()
print_card(player1_first_str, player1_second_str, player1_third_str)
card_1 = [player1_first_str, player1_second_str, player1_third_str]

print ("Карточка компьютера")
player2_first_str, player2_second_str, player2_third_str = card_generator()
print_card(player2_first_str, player2_second_str, player2_third_str)
card_2 = [player2_first_str, player2_second_str, player2_third_str]

# turns = [i for i in range(1,90)]
# def Game():
#     turn = turns[random.randint(0,89)]
#     if turn !=" " and turn != "-":
#         if turn in Card2:



   


