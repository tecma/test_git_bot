#!/usr/bin/python3


import os # работа с ос
import time # время
from subprocess import call # subprocess module (для прямой работы с sh)

# регулярки
import re


def git_looker():
    call (['git', 'pull'])
    time.sleep(3.5) # in seconds


while True:
    pass
    git_looker()


# git log --pretty=short


# нужна автопушилка коммитов
# нужна также тестовая автопушилка коммитов, создающая файлы и периодически затирающая их
# по-толковому нужны проверки на результат сразу же

#
#1. по таймеру проверять обновления в мастер ветке
#   если обновления есть, то вывести только автора\дату\файл\и внесённые изменения целиком
#   нужно как-то не выводить результаты проверки, если ничего нету
#
#2. если это док, то выводить полностью + кидать в лог и раскрывать лог при запуске скрипта,
#
#3.   если код -- делать так же но выводить не весь коммит, а только метку? или весь дифф?  
#   
# 
# добавить отрисовку отделяющих строк

# call (['git', 'status'])
# call (['git', 'log', '--pretty=short'])






# call (['ls', '-l'])



# def get_input(prompt):
#     while True:
#         s = raw_input(prompt)
#         if len(s) == 10 and set(s).issubset("abcdef"):
#             return s
#         print("The only valid inputs are 10-character "
#               "strings containing letters a-f.")