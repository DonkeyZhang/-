#-*-coding:utf-8-*-

# way01:
import random
all_choice = ['石头', '剪刀', '布']
win_list = [['石头','剪刀'], ['剪刀','布'],['布', '石头']]

computer = random.choice(all_choice)
player = input('请出拳(石头/剪刀/布):')
print(('你出拳: %s , 电脑出拳: %s') % (player, computer))

if computer == player:
    print('平局')
elif [player, computer] in win_list:
    print('YOU WIN!')
else:
    print('YOU LOSE!')

#way02:
import random
all_choice = ['石头', '剪刀', '布']
win_list = [['石头','剪刀'], ['剪刀','布'],['布', '石头']]

prompt=""" (0)石头
 (1)剪刀
 (2)布
 Please input your choice(0/1/2):""" # 提示预定义变量

computer = random.choice(all_choice) #电脑取值

ind = int(input(prompt))

player =all_choice[ind]
print(('你出拳: %s , 电脑出拳: %s') % (player, computer))

if computer == player:
    print('平局')
elif [player, computer] in win_list:
    print('YOU WIN!')
else:
    print('YOU LOSE!')