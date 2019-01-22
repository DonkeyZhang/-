#-*-coding:utf-8-*-
#1.功能:接受客户机连接.接受客户机发来的消息,把消息加上时间发回客户端
#2.流程:
# (1)创建class
# (2)class需要绑定哪些属性
# (3)class有那些


import  socket
from time import  strftime


class TcpTimeServer:
    def __init__(self,host='',port=1234):
        self.addr =(host,port)
        self.serv=socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def chat(self,cli_sock):
        while True:
            data =cli_sock.recv(1024)
            if data.strip()==b'quit':
                break
            data ='[%s] %s ' % (strftime('%H:%M:%S'),data.decode())




