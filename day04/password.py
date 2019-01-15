#-*-coding:utf-8-*-
##生成随机密码
# way01:
# import random
# def gen_pass(n=8):
#     number=''
#     password=''
#     for i in  range(n):
#         number=random.choice('1234567890qwertyuiopsdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
#         password+=number
#     return password
# if __name__ == '__main__':
#     a=gen_pass()
#     print(a)

##way02:
# import random
# import string
# all_chs=string.ascii_letters+string.digits
# def gen_pass(n=8):
#     number=''
#     password=''
#     for i in range(n):
#         number=random.choice(all_chs)
#         password+=number
#     return password
#
# if __name__ == '__main__':
#     a=gen_pass()
#     print(a)


#>>> import password
#>>> password.all_chs
#'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#import只导一次,退出来再导一次
#把不变的东西写函数外面
# help(shutil)
# yiyibooks.cn












