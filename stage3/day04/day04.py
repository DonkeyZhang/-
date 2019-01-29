#-*-coding:utf-8-*-
from urllib import  request

#1)获取一个html文件
# html=request.urlopen('http://www.tmooc.cn')
# with open('/zxw/Python/stage3/day04/tmooc.html','wb') as fobj:
#     while True:
#         data=html.read(1024)
#         if not data:
#             break
#         fobj.write(data)


#2)模仿浏览器访问
# header={'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0)\
#  Gecko/20100101 Firefox/52.0'}
# r = request.Request('http://127.0.0.1/', headers=header)
# html = request.urlopen(r)



#3)编码
# url = 'https://www.baidu.com/web?query=%s'
# param = request.quote('中国')
# html = request.urlopen(url % param)
# with open('/tmp/china.html', 'wb') as fobj:
#     fobj.write(html.read())

#4)处理异常信息
# from urllib import  request
# from urllib.error import HTTPError
#
# url1='http://127.0.0.1/abc/'
# url2='http://127.0.0.1/ban/'
# url3='http://127.0.0.1/'
#
# for  url in [url1,url2,url3]:
#
#     try:
#         html=request.urlopen(url)
#
#     except HTTPError as e: #把错误保存到变量里
#         print('错误',e)

#eog
#file

#pip3 intsall wget

# import wget
# wget.download('http://cdn.tmooc.cn/tmooc-web/css/img/tmooc-logo2.png')

import libvirt
# for vm in kvm.listall
#     kvm.list[2]
##########################################################
import re
import os
import  urllib.error
from urllib import  request

def download(url,fname):
     html = request.urlopen(url)
     with open (fname,'wb') as fobj:
         while True:
             data=fobj.read()
             if not data:
                 break
             fobj.write(data)

def get_url(fname,patt,encoding=None):
    url_list=[]
    cpatt=re.compile(patt)
    with open(fname,encoding=encoding) as fobj:
        for line in fobj:
            for m in cpatt.finditer(line):
                url_list.append(m.group())
    return  url_list


if __name__ == '__main__':
    net_url='http://www.163.com/'
    fname='/tmp/163.html'
    url_patt='(http|https)://[-\w./]+\.(png|jpg|jpeg|gif)'

    download(net_url,fname)

    url_list=get_url(fname,url_patt,encoding='gbk')

    folder='/tmp/wangyi'
    if not os.path.exists(folder):
        os.mkdir(folder)

    for url in url_list:
        fname = url.split('/')[-1]
        fname=os.path.join(folder,fname)
        try:
            download(url,fname)
        except urllib.error.HTTPError:
            print(url)



