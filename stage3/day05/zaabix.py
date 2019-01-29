#-*-coding:utf-8-*-
import  requests
import json



url='http://192.168.4.10/api_jsonrpc.php'
headers={'Content-Type': 'application/json-rpc'}


#1)
# data={
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 1
#
#     }


#2)
# data={
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }


#3)
data={
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": [
            "hostid",
            "host"
        ],
        "selectInterfaces": [
            "interfaceid",
            "ip"
        ]
    },
    "id": 2,
    "auth": "3268ef9f6fedc6777f0688caa287b210"
}
#结果
# data={
#     "jsonrpc": "2.0",
#     "result": [
#         {
#             "hostid": "10084",
#             "host": "Zabbix server",
#             "interfaces": [
#                 {
#                     "interfaceid": "1",
#                     "ip": "127.0.0.1"
#                 }
#             ]
#         }
#     ],
#     "id": 2,
    # "auth": "3268ef9f6fedc6777f0688caa287b210"
# }

#4)

#
# data={
#     "jsonrpc": "2.0",
#     "method": "item.create",
#     "params": {
#         "name": "Free disk space on $1",
#         "key_": "vfs.fs.size[/home/joe/,free]",
#         "hostid": "10084",
#         "type": 0,
#         "value_type": 3,
#         "interfaceid": "1",
#         "delay": 30
#     },
#     "auth": "3268ef9f6fedc6777f0688caa287b210",
#     "id": 3
# }
#5)

# data={
#     "jsonrpc": "2.0",
#     "method": "hostgroup.create",
#     "params": {
#         "name": "Linux haha"
#     },
#     "auth": "3268ef9f6fedc6777f0688caa287b210",
#     "id": 1
# }


#6)
data={
    "jsonrpc": "2.0",
    "method": "template.create",
    "params": {
        "host": "Linux lala",
        "groups": {
            "groupid": 1
        },
        "hosts": [
            {
                "hostid": "10084"
            },
            {
                "hostid": "10090"
            }
        ]
    },
    "auth": "3268ef9f6fedc6777f0688caa287b210",
    "id": 1
}

r=requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())


#组--->模板