#-*-coding:utf-8-*-
##从1加到100
# result = 0
# for i in range(1,101):
#     result +=i
# print(result)

##随机生成任意密码
# import random
# import string
# import sys
#
# all_chs=string.digits+string.ascii_letters
# word=''
# password=''
# def gen_pass(n=8):
#     word = ''
#     password = ''
#     for i in range(n):
#         word=random.choice(all_chs)
#         password+=word
#     return  password
#
#
# if __name__ == '__main__':
#     a=gen_pass(sys.argv[1])

##创建文件并存入数据
# import  os
#
# def get_fname():
#     while True:
#         fname = input('请输入文件名:')
#         if not os.path.exists(fname):
#             break
#         print('文件存在')
#     return  fname
#
# def get_content():
#     content=[]
#     while True:
#         line=input('>')
#         print('请输入数据')
#         if line == 'end':
#             break
#         content.append(line)
#     return content
#
# def wfile (fname,content):
#     with open(fname,'a') as fobj:
#         fobj.writelines(content)
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content=get_content()
#     content =[ '%s\n' % line for line in content]
#     wfile(fname,content)

##检查标识符

# import sys
# import string
# import keyword
# first_ch=string.ascii_letters+'_'
# others_ch=string.ascii_letters+'_'+string.digits
#
# def get_input(word):
#     if keyword.iskeyword(word):
#         return  '%s 是关键字' % word
#
#     if word[0]  not in first_ch:
#         print( '不合格的首字符')
#
#     for ind, ch in enumerate(word[1:]):
#         if ch not in others_ch:
#             return '第 %s 个字符不合格' % (ind+2)
#     return '%s 是个合格的字符' % word
#
#
# if __name__ == '__main__':
#     result=get_input(sys.argv[1])
#     print(result)


##格式化输出
# import mktxtfile
#
# width=48
#
# contents = mktxtfile.get_content()
#
# print('+%s+' %('*' * 48))
#
# for line in contents:
#     print('+{:^48}+'.format(line))
#
# print('+%s+' % ('*' * 48))

##调用系统命令 新建用户 随机密码 并将名字和密码写入文件
##adduser.py
# import sys
# import subprocess
# import password
#
# def add_user(username,password,userfile):
#     user_info=''' username: %s
# password: %s
# ''' % (username,password)
#     subprocess.call('useradd %s' % username,shell=True)
#     subprocess.call(
#         'echo %s |passwd --stdin %s' % (password, username),
#             shell=True
#     )
#     with open(userfile,'a') as fobj:
#         fobj.writelines(user_info)
#
#
# if __name__ == '__main__':
#     password=password.gen_pass(10)
#     add_user(sys.argv[1],password,'/file/user.txt')

## 判断是不是可不可以当作标识符
# def word_is_ringht():
#
#     a= input('请输入:')
#     if a.isidentifier():
#         print('可以当作字符')
#     else:
#         print('不合格的标识别法')
#     return   ' %s 可以当作字符' % a
# if __name__ == '__main__':
#









#值互换
# >>> a = 30
# >>> b =40
# >>> a,b = b,a
# >>> a ,b
# (40, 30)

##
# >>> list('hello')
# ['h', 'e', 'l', 'l', 'o']
# >>> tuple('hello')
# ('h', 'e', 'l', 'l', 'o')
# >>> str(100)
# '100'

##
# >>> import random
# >>> alist = [random.randint(1,100) for i in range(10)]
# >>> alist
# [99, 67, 77, 40, 64, 96, 65, 31, 10, 86]
# >>> max(alist)
# 99
# >>> min(alist)
# 10

##

# alist = ['bob', 'alice', 10, 20, 30]
#
# for ind in [0,1,2,3,4]:
#     print('%s: %s' % (ind, alist[ind]))
# for ind in range(5):
#     print('%s: %s' % (ind, alist[ind]))
# for ind in range(len(alist)):
#     print('%s: %s' % (ind, alist[ind]))
#
# print(enumerate(alist))
# print(list(enumerate(alist)))
#
# for item in enumerate(alist):
#     print('%s: %s' % item)
#
# print(reversed(alist))
# for item in reversed(alist):
#     print(item)
#
# print(sorted('hello'))

# >>> '%s is %s  years old' % ('bob',20)
# 'bob is 20  years old'
#
# >>> '97 is %c  years old' %  97
# '97 is a  years old'
#
# >>> '%s is %d' % ('bob', 20)
# 'bob is 20'
#
# >>> '%s is %o' % ('bob', 20)
# 'bob is 24'
#
# >>> '%s is %#o' % ('bob', 20)
# 'bob is 0o24'
#
# >>> '%s is %#d' % ('bob', 20)
# 'bob is 20'
#
# >>> '%s is %x' % ('bob', 20)
# 'bob is 14'
#
# >>> '%s is %#x' % ('bob', 20)
# 'bob is 0x14'
#
# >>> '100000 is %e' % 1000000
# '100000 is 1.000000e+06'
#
# >>> '5/2 is %d' % (5/2)
# '5/2 is 2'
#
# >>> '5/2 is %f' % (5/2)
# '5/2 is 2.500000'
#
# >>> '%10s%8d ' % ('bob',20)
# '       bob      20 '
# >>> '%-10s%-8d ' % ('bob',20)
# 'bob       20       '
#
#
# >>> '{} is {} years old'.format('haha',18)
# 'haha is 18 years old'
# >>> '{1} is {0} years old'.format('haha',18)
# '18 is haha years old'
# >>> '{0} is {0} years old'.format(['haha',18])
# "['haha', 18] is ['haha', 18] years old"
#
#
# ##
# >>> alist=  [10, 20, 30, 40, 50, [1,2,3]]
# >>> alist[-1]=20
# >>> alist
# [10, 20, 30, 40, 50, 20]
# >>> alist [1:3]=[20,30]
# >>> alist
# [10, 20, 30, 40, 50, 20]
# >>> alist [1:3]=[100,100]
# >>> alist
# [10, 100, 100, 40, 50, 20]
# >>> alist [1:1]=[100,100]
# >>> alist
# [10, 100, 100, 100, 100, 40, 50, 20]

