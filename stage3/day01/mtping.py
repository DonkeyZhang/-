#-*-coding:utf-8-*-
import  threading
import  subprocess


import subprocess
import os


def ping(host):
    rc = subprocess.call('pingng -c2 %s &> /dev/null' % host, shell=True)
    if rc ==0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)

if __name__ == '__main__':
    ips =('172.40.84.%s' % i  for i in range(1,255))
    for ip in ips:
        t = threading.Thread(target=ping,args=(ip,))
        t.start()

