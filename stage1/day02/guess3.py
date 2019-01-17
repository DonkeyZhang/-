#-*-coding:utf-8-*-
import random

number = random.randint(1, 100)
while 'a':
    man = int(input('请输入number:'))
    if  number < man:
        print('大了')
    elif number > man:
        print('小了')
    else:
        print('对了')
        break
print('This circe is done')
