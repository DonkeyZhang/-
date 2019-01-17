#-*-coding:utf-8-*-
import random

number = random.randint(1, 100)
running = True
while running:               #while 1 :
    man = int(input('请输入number:'))
    if  number < man:
        print('大了')
    elif number > man:
        print('小了')
    else:
        print('对了')
        running = False