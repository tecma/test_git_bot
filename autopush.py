#!/usr/bin/python3

# работа с ос
import os

# время
import time

# subprocess module (для прямой работы с sh)
from subprocess import call

# создание уникальных строк
import uuid; 

# for x in xrange(1,10):
#     pass




def file_toucher():
    x = uuid.uuid4()
    file_id = (str(x).upper()[0:6])

    gogo = open ("/home/tedudcaic/coding/projects/test_git_bot/pusher/"+file_id,"w")
    gogo.write(str(file_id))
    gogo.close()

    print('Created file with id: '+file_id)
    pass

file_toucher()


# x = uuid.uuid4()
# file_id = (str(x).upper()[0:6])

# print (file_id)








# def git_pusher(timer):
#     call (['git', 'push'])
#     time.sleep(timer) # in seconds