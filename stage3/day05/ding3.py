#-*-coding:utf-8-*-
#!/usr/bin/env python3

import json
import requests
# import sys

def send_msg3(url, reminders):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data={
        "msgtype": "markdown",
        "markdown": {"title": "杭州天气",
                     "text": "#### 杭州天气  \n > 9度，@1825718XXXX 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](http://www.thinkpage.cn/) "
                     },
        "at": {
            "atMobiles": reminders,
            "isAtAll": False
        }
    }

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text
if __name__ == '__main__':
    reminders = ['17717845806']  # 特殊提醒要查看的人,就是@某人一下
    url =  'https://oapi.dingtalk.com/robot/send?access_token=4af44454d5bd96012e249395f9cb9dd9e13c49d86dc1e781c2fcaffc9ab7d5c2'
    #此处填写上面第5步webhook的内容
    print(send_msg3(url, reminders))