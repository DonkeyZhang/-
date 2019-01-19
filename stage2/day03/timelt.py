#-*-coding:utf-8-*-
import  time

from tqdm import tqdm

def deco(func):
    def timeit():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return timeit

@deco
def myadd():
    result = 0
    for i in tqdm(range(20000000)):
        result+=1
    print(result)

if __name__ == '__main__':
    # start=time.time() #开始时间
    # myadd()
    # end=time.time() #结束时间
    # a=end-start
    # print(a)
    #timeit(myadd)
    # myadd=deco(myadd)
    # print(myadd())
    myadd()