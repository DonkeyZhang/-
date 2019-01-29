#-*-coding:utf-8-*-
from  email.mime.text import MIMEText
from email.header import Header
import  smtplib
import  getpass

message = MIMEText('Python邮件测试\r\n','plain','utf8')#消息内容
message['From']=Header('zhangxinwan01@163.com','utf8')#消息内容的发送者
message['To']=Header('root@localhost','utf8')         #消息内容的收件者
message['Subject']=Header('Welcome','utf8')          #消息内容的标题
password=getpass.getpass()                           #密码

#smtp=smtplib.SMTP('localhost')   #使用本地服务器

smtp=smtplib.SMTP()                  #转发的服务器
smtp.connect('smtp.163.com')         #连接服务器 web页面查看
smtp.login('zhangxinwan01@163.com',password) #登陆服务器

#smtp.starttls()                   #如果服务器要求安全通信,打开此通信

sender='zhangxinwan@163.com'       #消息的发送用户
receivers =['zhangxinwan01@163.com']#消息的收件者

smtp.sendmail(sender,receivers,message.as_bytes())#发送邮件,以byte发送