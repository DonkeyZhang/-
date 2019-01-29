#-*-coding:utf-8-*-
#类
#
# class Vendor:
#     def __init__(self,company,ph):
#         self.company=company
#         self.phone=ph
#
#     def call(self):
#         print('Calling %s...' % self.phone)
#
# class PigToy:
#     def __init__(self,name,color,company,ph):
#         self.name=name
#         self.color=color
#         self.vedor=Vendor(company,ph)
#
#     def show_me(self):
#         print('%s is %s' % (self.name,self.color))

#piggy=PigToy('lala','black','kk','40000')
#piggy.show_me()
#piggy.vedor.call()


# class Book:
#
#     def __init__(self,name,author):
#         self.name=name
#         self.author=author
#
#     def __str__(self):
#         return (' %s  is  %s' % (self.name,self.author))
#
#     def __call__(self):
#         print('%s is %s' % (self.name,self.author))
#
# if __name__ == '__main__':
#     a=Book('haha','kk')
#     print(a)
#     a()

# import  hashlib
# import sys
# m=hashlib()
#
# def md5_sum(fname):
#
#     with open(fname,'rb') as fobj:
#
#         while True:
#             data=fobj.read(4096)
#             if data == 0:
#                 break
#             m.update(data)
#     return m.hiexdigest
#
# if __name__ == '__main__':
#     md5_sum(sys.argv[1])

# class A:
#     def show1(self):
#         print('haha')
#
# class B:
#     def show2(self):
#      print('xixi')
#
# class C(B,A):
#     def show3(self):
#         print('lala')
#
#

# a=C()
# a.show2()
##

#
# import time
# from tqdm import tqdm
#
# def deco(func):
#     def timeit():
#         starttime=time.time()
#         func()
#         endtime=time.time()
#         print(endtime-starttime)
#     return timeit
#
# @deco
# def myadd():
#     result=0
#     for i in tqdm(range(10000000000)):
#         result+=i
#     print(result)
#
# if __name__ == '__main__':
#     myadd()




