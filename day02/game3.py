#-*-coding:utf-8-*-
counter = 1
user = 0
com =0
while counter <= 3:
    import random
    all_choice = ['石头', '剪刀', '布']
    win_list = [['石头','剪刀'], ['剪刀','布'],['布', '石头']]

    prompt=""" 
    (0)石头
    (1)剪刀
    (2)布
    Please input your choice(0/1/2):"""

    computer = random.choice(all_choice)

    ind = int(input(prompt))

    player =all_choice[ind]
    print(('你出拳: %s , 电脑出拳: %s') % (player, computer))

    if computer == player:
        print('平局')
        continue
    elif [player, computer] in win_list:
        print('YOU WIN this time!')
        user+=1
        if user == 2:
            print( 'you is winner!')
            break
        else:
            counter += 1
    else:
        print('computer win this time!')
        com += 1
        if com == 2:
            print('computer is winner!')
            break
        else:
            counter += 1

