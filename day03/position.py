#-*-coding:utf-8-*-
import sys #导入sys
print(sys.argv)                  #是个列表

for i in range(len(sys.argv)):   #位置变量有几个被占
    print(sys.argv[i])           #显示每一个位置的有哪些数
