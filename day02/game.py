#-*-coding:utf-8-*-
import random
number = random.choices(['石头', '剪刀', '布'])
player = input('请出拳(石头/剪刀/布):')
print('你出拳: %s, 计算机出拳: %s' % (player ,number))

if player == '石头':
    if number == '石头':
        print( '平局')
    elif number == '剪刀':
        print('YOU WIN!')
    else:
        print('YOU LOSE!')
elif player == '剪刀':
    if number == '剪刀':
        print( '平局')
    elif number == '石头':
        print('YOU LOSE')
    else:
        print('YOU WIN!')
else:
    if number == '布':
        print( '平局')
    elif number == '剪刀':
        print('YOU LOSE!')
    else:
        print('YOU WIN!')

