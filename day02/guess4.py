#-*-coding:utf-8-*-

import random

number = random.randint(1, 3)
counter = 0
while counter < 3:
    man = int(input('请输入number:'))
    if  number < man:
        print('大了')
    elif number > man:
        print('小了')
    else:
        print('对了')
        break
    counter += 1
else:
    print( 'answer:',number)

print('This circe is done')