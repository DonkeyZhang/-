#-*-coding:utf-8-*-
import os

print('hello world!')

ret_val =os.fork()            #父进程复制产生了一个子进程 ,剩下的既在父进程里执行也在子进程里执行
#print('how are you!')#都是在终端输出

if ret_val:
    print('hello  from parent ')
else:
    print('hello from child')

print('hello from both')

# hello world
# how are you
# how are you