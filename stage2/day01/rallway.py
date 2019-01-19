#-*-coding:utf-8-*-
import time

print('#' * 20,end='')
n = 0

while True:
    time.sleep(0.3)
    print('\r%s@%s' % ('#' * n, '#' * (19 -n)), end='')
    n += 1
    if n == 20:
        n =0           #如果等于20的时,将n改为0

#简书124






