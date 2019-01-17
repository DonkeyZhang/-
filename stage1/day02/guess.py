#-*-coding:utf-8-*-
#way01:
import  random

number = random.randint(1, 10)
print(number)

answer = int(input('number:'))

if answer > number:
    print('猜大了')
elif answer < number:
    print('猜小了')
else:
    print('猜对了')

#way02
import random

number = random.randint(1, 10)
print(number)

keyboard = int(input('number:'))
if  number > keyboard:
    print('大了')
elif number < keyboard:
    print('小了')
else:
    print('对了')

