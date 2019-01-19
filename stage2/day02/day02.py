#-*-coding:utf-8-*-
#
#import  os
#os.mkdir('/tmp/abcd') #建议调用这个, 跨平台
###########################################################
##
import os
import pickle
import time


def save(fname):
    amount=input('amount:')
    comment=input('comment:')
    date=time.strftime()
    with open(fname,'rb') as fobj:
        pickle.dump()


def cost(fname):





def show_menu():

    prompt=''' (0) cost
    (1) save
    (2) query
    (3) quit
    please input your choice (0/1/2/3):'''

    fname='account.data'

    if not os.path.exists(fname):
        init =[time.strftime(),0 , 0, 0, 'init']
        with open(fname,'wb') as fobj:
            pickle.load(fobj)

    cmds={'0':'save', '1':'cost' , '2':'query'}

    while True:
        choice=input(prompt)

        if choice not in '0123':
            print('Invalid input.')
            continue
        if choice =='3':
            break
        cmds[choice](fname)
if __name__ == '__main__':
    show_menu()























#  def foo():
#     print('in foo')
#     bar()
# foo()
#
# def bar():
#     print('')
#
# def set_age(set_name,)
# 函数:
#
# >>> def set_age(name,age):
# ...      print ('%s is %s years old' % (name,age))
# ...
# >>> set_age('bob',20)
# bob is 20 years old
# >>> set_age(20,20)
# 20 is 20 years old
# >>> set_age(20,'bob')
# 20 is bob years old
# >>> set_age(name=20,age='bob')
# 20 is bob years old
# >>> set_age(20,age='bob')
# 20 is bob years old
#
# >>> set_age(age='bob',20)   #age后面
#   File "<stdin>", line 1
# SyntaxError: positional argument follows keyword argument
#
# >>> set_age(20,name=20)     #name指向两个值
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: set_age() got multiple values for argument 'name'

#######################################################
#
#  def  myfunc(*args):         #*表示元组
#     print(*args)
#
# def myfunc2(**kwargs):
#     print(kwargs)
#
# if __name__ == '__main__':  #参数将会放到元组中 args=('hello')
#     myfunc()  #args
#     myfunc('hello')     #参数将会放到元组中 args=('hello',)
#     myfunc('hello',123) #参数将会放到元组中 args=('hello',123)
#
#     myfunc2()
#     myfunc2(name='hello')
#     myfunc2(name='bob',age=23 )
#########################################################
#
#  def add(x, y):
#     print(x + y)
#
# if __name__ == '__main__':
#     add(10, 20)
#     nums =[10 ,20]
#     add(nums[0],nums[1])
#     add(*nums)     #表示把num拆开
########################################################
#
# def add(x,y):
#     return  x+y
#
# if __name__ == '__main__':
#     print(add(1,20))
#     a=lambda x,y:x+y
#     print(a(20,30))
########################################################
#
# import  random
#
# def func1(x):
#     return  x % 2 #结果是1是0 表示True和Flase
#
# def func2(x):
#     return  x * 2 +1
# if __name__ == '__main__':
#     nums =[random.randint(1,100) for i in range(10)]
#     print(nums)
#
#     print(list(filter(func1,nums)))
#     print(list(filter(lambda x:x % 2, nums)))
#     # filter是实现过滤,将nums中的每一项当成func1的参数.func1的结果为真.则把数字留下
#
#     print(list(map(func2, nums)))
#     print(list(map(lambda x: x *2 +1,nums)))
#     #map用来加工数据. 将nums中的每一个项目作为func2的参数惊醒加工,得到结果
#####################################################################
#
# from functools import partial
# def  add(a, b, c, d):
#     print(a+b+c+d)
#
# if __name__ == '__main__':
#     add(10,20,30,5)
#     add(10,20,30,8)
#     add(10,20,30,11)
#     add(10,20,30,14)
#     myadd =partial(add,10,20,30)
#     myadd(5)
#     myadd(8)
#     myadd(11)
#     myadd(14)
#
#############################################
#
#
# def func1(x):
#     if x == 1:
#         return 1  #
#     return x * func1(x - 1) #
#
#     #  5 * func1(4)
#     #  5 * 4 * func1(3)
#     #  5 * 4 * 3 * func1(2)
#     #  5 * 4 * 3 * 2 * func1(1)
#     #  5 * 4 * 3 * 2 * 1
#
# if __name__ == '__main__':
#     print(func1(5))
#     print(func1(6))
###################################### 生成齐
