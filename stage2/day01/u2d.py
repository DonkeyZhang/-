#-*-coding:utf-8-*-
#hello world\n --> hello world

import  sys

def unix2dos(fname):
    dst_fanme= fname+'.txt'

    with open(fname,'r') as src_fobj:
        with open(dst_fanme,'w') as  dst_fobj:

            for line in src_fobj:
                line =line.rstrip()+'\r\n'   #每一行的\r\n 去掉加上\r\n
                dst_fobj.write(line)         #表示回车不换行

if __name__ == '__main__':
    unix2dos(sys.argv[1])