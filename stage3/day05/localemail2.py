#-*-coding:utf-8-*-
from  email.mime.text import MIMEText
from  email.header import Header
import  smtplib
import  getpass

def send_email(text,subject,sender,receivers,mail_host,password):

    message = MIMEText()         #消息内容
    message['From']=Header(sender,'utf8')             #消息内容的发送者
    message['To']=Header(receivers[0],'utf8')         #消息内容的收件者
    message['Subject']=Header(subject,'utf8')         #消息内容的标题
    # password=getpass.getpass()                        #密码


    smtp=smtplib.SMTP()               #转发的服务器
    smtp.connect(mail_host)           #连接服务器 web页面查看
    # smtp.starttls()                 #如果服务器要求安全通信,打开此通信
    smtp.login(sender,password)       #登陆服务器
    smtp.sendmail(sender,receivers,message.as_bytes())#发送邮

if __name__ == '__main__':
    mail_host='smtp.qq.com'
    sender='643794886@qq.com'
    password=getpass.getpass()
    receivers=['643794886@qq.com']
    subject='Welcome to Tedu!'
    text='Python 邮件测试\r\n'
    send_mail=(text,subject,sender,receivers,mail_host,password)
