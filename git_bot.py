#!/usr/bin/python3

# работа с ос
import os

# время
import time

# subprocess module (для прямой работы с sh)
from subprocess import call

# регулярки
import re


def git_looker():
    time.sleep(3) # in seconds
    call (['git', 'pull'])



# git log --pretty=short


#
#1. по таймеру проверять обновления в мастер ветке
#   если обновления есть, то вывести только автора\дату\файл\и внесённые изменения целиком
#
#2. если это док, то выводить полностью + кидать в лог и раскрывать лог при запуске скрипта,
#
#3.   если код -- делать так же но выводить не весь коммит, а только метку? или весь дифф?  
#   
# 
# добавить отрисовку отделяющих строк

# call (['git', 'status'])
call (['git', 'log', '--pretty=short'])






# call (['ls', '-l'])



# def get_input(prompt):
#     while True:
#         s = raw_input(prompt)
#         if len(s) == 10 and set(s).issubset("abcdef"):
#             return s
#         print("The only valid inputs are 10-character "
#               "strings containing letters a-f.")