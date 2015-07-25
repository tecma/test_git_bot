#!/usr/bin/python3

import os, time, re # работа с ос, время, регулярки
from subprocess import call # subprocess module (для прямой работы с sh)


def git_looker():
    call (['git', 'pull'])
    time.sleep(1) # in seconds


while True:
    pass
    git_looker()


# справки см. внизу под всем этим

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


# git log --help
# git log --graph --oneline --decorate --all


# привязка к удалённому репо: 
# git remote add origin https://github.com/username/your-project.git


# use colorful git output
# git config color.ui true

# если первый коммит, то -- "git push -u origin feature/name-of-branch" ()
# чтобы привязать локальную ветку к ветке на github
# впоследствии ключ -u не нужен


# git log --pretty=short
# git log --pretty=format:'FORMAT'
# Определение формата можно поискать в разделе по git log из Git Community Book




# http://hexvolt.blogspot.ru/2014/01/git-1.html 

# Находясь в ветке "clean_up", произведем изменения проекта - удалим файл "README.md":
#     git rm README.md
# Эта команда не просто удалит файл с диска, но и зафиксирует его отсутствие в staging area (снимет с наблюдения). 
# Примечание: для удаления папки со всем ее содержимым используется ключ -r (рекурсия): "git rm -r <folder>". Если просто удалить файл с диска, то запись о нем останется в staging area, и для ее удаления все равно придется применять команду rm. 

# После внесения изменений делаем коммит ветки "clean_up":
#     git commit -m "Remove file README.md"

# Допустим, мы завершили редактирование всех необходимых изменений, убедились в работоспособности проекта и теперь хотим объединить ветки, проапргедив главную ветку "master". Для этого нужно на нее переключится:
#     git checkout master

# Обратите внимание, что после этой команды все файлы рабочей папки django_project вернутся в прежнее состояние (в нашем примере - появится файл README.md). Теперь подтягиваем сюда изменения из ветки "clean_up":
#     git merge clean_up

# Коммит из ветки "clean_up" добавится в основную ветку "master". 