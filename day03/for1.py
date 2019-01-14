#-*-coding:utf-8-*-
py_str = 'python'
alist = [10, 20, 30]
atuple = ('bob' , 'alice', 'tom')
adict = {'name':'zhangsan', 'age':22}
for i in py_str:
    print(i)

for i in alist:
    print(i)

for i in atuple:
    print(i)

for i in adict:
    print('%s: %s' % (i, adict[i]))