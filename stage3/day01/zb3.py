#-*-coding:utf-8-*-
import os
import  time


print('start...')
ret_val=os.fork()

if ret_val:
    print('in parent')
    time.sleep(20)
    os.waitpid(-1,1)
    time.sleep(20)
    print('parent done')
else:
    print('in child')
    time.sleep(30)
    print('child done')