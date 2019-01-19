#-*-coding:utf-8-*-
import  hashlib
import  sys

def check_md5(fname):

    m = hashlib.md5()

    with open(fname ,'rb')  as fobj:
        while True:
            data = fobj.read(4096)
            if  not data:
                break
            m.update(data)
        return  m.hiexdigest()

if __name__ == '__main__':
    check_md5(sys.argv[1])


