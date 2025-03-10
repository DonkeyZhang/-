#-*-coding:utf-8-*-
from random import  randint

def qsort(seq):

    if len(seq) < 2:
        return  seq #sdd如果序列长度小于2,直接返回该序列对象

    middle=seq[0]
    smaller =[]
    larger = []

    for item  in seq[1:]:

        if item <=middle:
             smaller.append(item)
        else:
            larger.append(item)

    return qsort(smaller) + [middle] +qsort(larger)

if __name__ == '__main__':
    nums = [randint(1,100) for i in range(10)]
    print(nums )
    print(qsort(nums))