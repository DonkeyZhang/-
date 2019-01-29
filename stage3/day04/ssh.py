#-*-coding:utf-8-*-

import paramiko

import sys

import getpass

import os

import threading


def rcmd(host,user='root',passwd=None,cmd=None):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,username=user,password=passwd)

    stdin,stdout,stderr=ssh.exec_command(cmd)
    out=stdout.read()
    err=stderr.read()

    if out:
        print('[%s] OUT:\n%s' % ( host, out.decode()))
    if err:
        print('[%s] ERR:\n%s' % (host,err.decode()))


if __name__ == '__main__':
    if len(sys.argv) !=3:
        print('Usage:%s ipfile "command" ' % sys.argv[0])
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('No such file:',sys.argv[1])
        exit(2)

    ipfile =sys.argv[1]
    command=sys.argv[2]
    #password=getpass.getpass()
    password='123456'

    with open(ipfile) as fobj:
        for line in fobj:
            ip =line.strip()

            t=threading.Thread(target=rcmd,args=(ip,'root',password, command))
            t.start()




# rcmd('192.168.4.33',passwd='123456',cmd='id root;id zhangsan')

# ip=['192.168.4.31','192.168.4.32','192.168.4.33']
# for node in ip:
#     ssh =paramiko.ssh
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 回答yes
#
#     os.fork()
#
#     ssh.connect(node, username='root', password='123456')
#     ssh.exec_command('mkdir /tmp/demo')
#     ssh.close()
#     exit()
# ssh.connect(ip, username='root', password='123456')
# result = ssh.exec_command('id root; id zhangsan')
# len(result)