#!/usr/bin/python3

import os, time, uuid # работа с ос, время, регулярки, создание уникальных строк
from subprocess import call # subprocess module (для прямой работы с sh)

exec_path = os.path.abspath(os.curdir)
files_path = exec_path+'/pusherfiles/'
# нужно проверять количество файлов, и если их накапливается 10 штук, делать микропаузу, потом пушить
# без стеджа и ждать 2 минуты, потом затирать все файлы в папке, и по-новой
# похоже нужен отдельный каунтер (его можно ретурнить из прока и обернуть всё это в while)



def file_toucher(): # создаём случайные файлы

    file_id = (str(uuid.uuid4()).upper()[0:6]) # создаём уникальный id

    touch = open(files_path+file_id,"w") # создаём файл с этим ид
    touch.write(str(file_id)) # записываем в него id 
    touch.close()

    print('Создан случайный файл с ID: '+file_id)
    pass


def git_pusher():
    os.chdir(files_path)
    if (len(files_path) >= 2):
        call (['git', 'add', '*'])
        time.sleep(1.5) # in seconds
        call (['git', 'commit', '-a', '--allow-empty-message', '-m', ' ' ])
        time.sleep(1.5)
    else:
        print ('Надо набрать 3 файла')


def proc(file_count):

    file_count

    while True:
            time.sleep(1.2)
            file_toucher()
            file_count = file_count + 1
            # print (file_count)

            if file_count == 2:
                print('Создано ' + str(file_count) + ' случайных файла.')
                break  

proc(0)
git_pusher()


# if len(touch)


    # if file_count < 10:
    #     proc(0)
    # else:

    #     # remove('/home/tedudcaic/coding/projects/test_git_bot/pusher/*')   



# def git_pusher(timer):
#     call (['git', 'push'])
#     time.sleep(timer) # in seconds