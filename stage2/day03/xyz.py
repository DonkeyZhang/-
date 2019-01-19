#-*-coding:utf-8-*-
import  sys
import  hashlib
m = hashlib.md5(b'123456')
m.hexdigest()


>>> import hashlib


>>> m=hashlib.md5(b'123qqq...A')
>>> m.hexdigest()
'e30bee35e11ad8809e36ffe0984c6280'


>>> with open('/etc/passwd','rb') as fobj:
...     data=fobj.read()
...
>>> m = hashlib.md5(data)
>>> m.hexdigest()
'65c68e5b0ec8b296d0b4079c45ea41fd'

