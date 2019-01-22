#-*-coding:utf-8-*-
#

import  re                          #re模块,匹配正则, re.search('f..','food')
#from collections import  Counter
import  collections                 #统计次数

def count_patt(fname,patt):         #fname文件名,patt为参数要查询的查询

    #patt_dict= {}                  #存入字典
    cpatt = re.compile(patt)        #要找的patt表达式 执行效率高

    counter=collections.Counter()   #调用统计函数

    with open(fname) as fobj:

        for line in fobj:          #对每条数据进行查找

            m=cpatt.search(line)   #找到了赋值给m

            if m:                 ##mygroup() 为一个IP,找到了 统计一下次数
                counter.update([m.group()])
                #key=m.group()
                #patt.dict[key]=patt_dict.get(key,0)+1

# >> > from collections import Counter
# >> > c = Counter()
# >> > c.update(['192.168.20.3'])
# >> > c.update(['192.168.20.3'])
# >> > c.update(['192.168.20.3'])
# >> > c.most_common(3)
# [('192.168.20.3', 3)]
# >> > print(c)
# Counter({'192.168.20.3': 3})

        return counter  #返回字典,统计的次数


if __name__ == '__main__':

    fname='access_log'          #统计的文件
    ip='^(\d+\.){3}d+'          #找ip的正则,0.0.0.0---?\d+ 至少一个数字(\d+.)作为一个整体(\d+.){3} 匹配三次
    br='Chrome|Friefox|MSIE'    #浏览器是这几个
    print(count_patt(fname,ip))
    print(count_patt(fname,br))