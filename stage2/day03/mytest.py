# -*-coding:utf-8-*-
import os     #按字母顺序改的
import time   #
              #

def show_time(format='%H:%M:%S'):
    pwd = os.getcwd()
    print(pwd)
    print(time.strftime(format))
