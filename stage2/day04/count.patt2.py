#-*-coding:utf-8-*-
#面向对象
#
import  re
from collections import Counter

class CounterPatt:                      #创建类
    def __init__(self, fname):          #创建实例,用来使用方法
        self.fname =fname               #文件名
#self.cpatt =re.compile(patt)

    def count_patt(self,patt):          #patt参数

        patt_counter =Counter()         #

        cpatt = re.compile(patt)

        with open (self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)

                if m:
                    patt_counter.update([m.group()])

        return patt_counter

if __name__ == '__main__':
    fname ='access_log'
    ip = '^(\d+\.){3}d+'
    br = 'Chrome|Friefox|MSIE'
    cp =CounterPatt(fname)               #创建实例
    print(cp.count_patt(ip))             #使用方法
    print(cp.count_patt(br))