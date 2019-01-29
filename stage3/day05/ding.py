#-*-coding:utf-8-*-
#!/usr/bin/env python3

import json
import requests
import sys

def send_msg1(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",  # 发送消息类型为文本
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,   # 不@所有人
        },
        "text": {
            "content": msg,   # 消息正文
        }
    }

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text

if __name__ == '__main__':
    msg = sys.argv[1]
    reminders = ['17717845806']  # 特殊提醒要查看的人,就是@某人一下
    url =  'https://oapi.dingtalk.com/robot/send?access_token=4af44454d5bd96012e249395f9cb9dd9e13c49d86dc1e781c2fcaffc9ab7d5c2'
    #此处填写上面第5步webhook的内容
    #print(send_msg(url, reminders, msg))
    print(send_msg1(url, reminders,msg))