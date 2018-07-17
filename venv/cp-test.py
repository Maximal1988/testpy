import os ### Модуль оси
import psutil ### модуль сторонний для получения списка процесов
import sys
import platform

print ("Maximal applications")

name = input("Привет, как тебя зовут ?")
print (name, "добропожаловать")

# pep-8
answer = input ("Давай поработаем ? (Y/N)")
if answer == 'y':
    print("Что будем делать ?")
    print("1 - Вывести список файлов и каталогов в текущем каталоге")
    print("2 - Вывести информацию о системе")
    print("3 - Вывести список процесов (pid)")



    do = int (input ("Укажите номер действия: "))
    if do == 1:
        print (os.listdir())
    elif do == 2:
        print(f'Имя текущей директории: {os.getcwd()}')
        print(f"Платформа (ОС): {os.name}")
        print(f"Платформа (ОС): {sys.platform}")
        print(f"Платформа (ОС): {platform.uname()}")
        print(f"Кодировка файорврй системы: {sys.getfilesystemencoding()}")
        print(f"Имя текущего пользователя в системе: {psutil.users()}")
        print(f"Количество ядер у процессора {os.cpu_count()}")
    elif do == 3:
        print(psutil.pids())
    else:
        print("Выбирите один из пунктов меню!")
elif answer == 'n':
    print("окай (")
else :
    print ("Давай подумаем еще")