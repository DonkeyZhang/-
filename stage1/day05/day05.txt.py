#-*-coding:utf-8-*-
##石头 剪刀 布
##三局两胜
##game.py
# import random
#
# all_chs=['石头', '剪刀' ,'布']
#
# computer=random.choices(all_chs)
#
# win_items=[['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
#
# pwin = 0
# cwin = 0
# prompt = '''
#     [0]石头
#     [1]剪刀
#     [2]布
#     请输入0/1/2:'''
# while True:
#     ind=input(prompt)
#     if all_chs[int(ind)] ==computer:
#         print('平局')
#         continue
#     elif [all_chs[int(ind)],computer] in win_items:
#         print('YOU WIN')
#         pwin+=1
#         if pwin == 2:
#             print('people win 2 times')
#             break
#     else:
#         print('computer  win')
#         cwin += 1
#         if cwin == 2:
#             print('computer win 2 times')
#             break

##猜数程序
# import random
# computer = random.randint(1,101)
# while True:
#     number = int(input('number:'))
#     if number > computer:
#         print('大了')
#
#     elif number < computer:
#         print('小了')
#     else:
#         print('猜对了')
#         print('answer: %s' % computer)
#         break

##斐波那契数列
##fib.py
# alist = [0, 1]
# n=int(input('次数:'))
# for i in range(n-2):
#     alist.append(alist[-1]+alist[-2])
# print(alist)

##九九乘法表
#mtable.py
# n=int(input('你的乘法表:' ))
# for i in range(1,n):
#     for j in range(1,i+1):
#         print('%sX%s=%s' % (j,i,j*i),end=' ')
#     print()

##模拟cp操作
## cp.py
##way01:
# f1=open('/bin/ls','rb')
# f2=open('/file/ls.txt','wb')
#
# data=f1.read()
# f2.write(data)
#
# f1.close()
# f2.close()

##way02:
# with open('/bin/ls','rb') as fobj1:
#     with open('/file/ls2.txt','wb') as fobj2:
#         data=fobj1.read()
#         fobj2.write(data)

##way03:

# import sys
#
# def cp_py(src_name,dst_name):
#
#     with open(src_name,'rb') as fobj1:
#         with open(dst_name,'wb') as fobj2:
#             data=fobj1.read()
#             fobj2.write(data)
#
#         return fobj2
#
#cp_py(sys.argv[1],sys.argv[2])

##生成随机密码
##




