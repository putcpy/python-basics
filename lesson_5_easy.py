import shutil
import sys
import os

def dirmaker():
    name = input("введите название папки")
    # таким был бы код для easy, но в таком виде, я не понимаю, как применить его в medium
    # for i in range(1, 10):
    #     os.mkdir("dir_" + str(i))
    try:
        os.makedirs(name)
    except FileExistsError:
        print("Такая папка уже есть")

def dirdestroyer():
    name = input("введите название папки")
    # таким был бы код для easy, но в таком виде, я не понимаю, как применить его в medium
    # for i in range(1, 10):
    #     os.rmdir("dir_" + str(i))
    try:
        os.rmdir(name)
    except FileExistsError:
        print("нет такой папки")

def showlist():
    print(os.listdir())

def filecopy():
    original = sys.argv[0]
    copy = original + '.copy'
    shutil.copy(original,copy)

