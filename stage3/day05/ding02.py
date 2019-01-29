#-*-coding:utf-8-*-
#!/usr/bin/env python3

import json
import requests
# import sys

def send_msg2(url, reminders):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data={
        "msgtype": "link",
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,  # 不@所有人
        },
        "link": {
            "text": "群机器人是钉钉群的高级扩展功能。群机器人可以将第三方服务的信息聚合到群聊中，实现自动化的信息同步。例如：通过聚合GitHub，GitLab等源码管理服务，实现源码更新同步；通过聚合Trello，JIRA等项目协调服务，实现项目信息同步。不仅如此，群机器人支持Webhook协议的自定义接入，支持更多可能性，例如：你可将运维报警提醒通过自定义机器人聚合到钉钉群。",
            "title": "自定义机器人协议",
            "picUrl": "",
            "messageUrl": "https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.Rqyvqo&treeId=257&articleId=105735&docType=1"
        }
    }

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text

if __name__ == '__main__':

    reminders = ['17717845806']  # 特殊提醒要查看的人,就是@某人一下
    url =  'https://oapi.dingtalk.com/robot/send?access_token=4af44454d5bd96012e249395f9cb9dd9e13c49d86dc1e781c2fcaffc9ab7d5c2'
    #此处填写上面第5步webhook的内容
    print(send_msg2(url, reminders))