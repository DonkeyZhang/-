#-*-coding:utf-8-*-
##三局两胜



##斐波那契数列
# def fib(length=8):
#     fib=[0,1]
#     for i in range(length -2 ):
#         fib.append(fib[-1]+fib[-2])
#     return fib
#
# if __name__ == '__main__':
#         fib()

##九九乘法表
#for循环
# for i in range(1,10):
#     for j in  range(i+1):
#         print('%sx%s=%s' % (j,i,i*j),end=' ')
#     print()

##输出192.168.1.0/网段
#列表解析
#print(['192.168.1.' + str(i) for i in range(1,255)])

##打开文件,读写文件,关闭文件

# >>> fobj =open('/mnt/passwd','r')
# >>> data =fobj.read()           #默认读完
# >>> print(data)                 #输出结果
# >>> data =fobj.read()           #指针已经指向最后了,读的是
# >>> print(data)
# >>> fobj.close()

##读文本文件
# fobj=open('/mnt/passwd','r')
# data=fobj.read()
# print(data)
# fobj.close()

##读程序
# fobj=open('/bin/ls','rb')
# data=fobj.read(4096)       #读4096字节 4k
# print(data)
# fobj.close()

##读行
# fobj=open('/mnt/passwd','r')
# data=fobj.readline()
# print(data,end=' ')
#fobj.close()

##重写文件 'w' 清空再写入
# >>> fobj=open('/mnt/passwd','w')
# >>> data=fobj.write('hello world!')
# >>> fobj.flush()
# >>> fobj.close()
# >>> fobj=open('/mnt/passwd','r')
# >>> print(fobj.read())
# hello world!

##追写文件 'a',追加到最后写入
# >> fobj=open('/mnt/passwd','a')
# >>> data=fobj.write('hello world!')
# >>> fobj.flush()
# >>> data=fobj.write('hello world!')
# >>> fobj.flush()
# >>> fobj

##列表写入writelines()
# >>> fobj=open('/mnt/passwd','w')
# >>> data=fobj.writelines(['hello world\n','3333\n'])
# >>> fobj.flush()
# >>> fobj.close()

##with语句 简化代码 代码块执行完 关闭文件
# with open('/etc/passwd','r') as fobj:
#     data = fobj.read()
#     print(data)

##文件内移动 seek(number,0/1/2)
# >>> fobj=open('/mnt/passwd','rb')
# >>> data=fobj.seek(2,0)
# >>> print(data)
# 2
# >>> fobj.close()

##实现cp.py
# src_fname = '/bin/ls'
# dst_fname = '/mnt/list'
#
# with open(src_fname,'rb') as fobj1:
#     with open(dst_fname,'wb') as fobj2:
#         src_data = fobj1.read()
#         fobj2.write(src_data)

##实现cp.py.传参数
# import  sys
# def cp(src_name,dst_name):
#     with open(src_name,'rb') as fobj1:
#         with open(dst_name,'wb') as fobj2:
#             while True:
#                 src_data = fobj1.read(4096)
#                 if src_data == 0:
#                     break
#                 fobj2.write(src_data)
# cp(sys.argv[1],sys.argv[2])

##star 打印星星
# def pstar(length=8):
#     print('*' * length)
#
# pstar()
# pstar(9)

##用户随机生成不同位的密码
# def password(length = 8):
#     import random
#     import string
#     all_ch=string.digits+string.ascii_letters
#     number = ''
#     password = ''
#     for i in range(length):
#         number=random.choice(all_ch)
#         password+=number
#     return password
#print(password())

#调用
# import randpass
# print(randpass.password(18))

























# def add():
#     result = 3 + 4    #局部变量
#
# a = add()
# print(a)      #None 没有返回值
# print(result) #报错
