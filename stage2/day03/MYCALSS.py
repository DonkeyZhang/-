#-*-coding:utf-8-*-
class A:
    def foo(self):
        print('foo')
    def hi(self):
        print('hello')

class B:
    def bar(self):
        print('bar')
    def hi(self):
        print('你好')
class C(A,B):
    def hi(self):
        print('ni hao')

c1 = C()

c1.foo()
c1.bar()

c1.hi()