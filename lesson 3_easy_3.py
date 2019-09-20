# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def str_lang_counter():
    user_list_input = input("введите что-то в любом количестве через запятую, не используя пробелы ")
    user_list = user_list_input.split(',')
    print(max(user_list, key=len))

str_lang_counter()