#-*-coding:utf-8-*-
import  re
from urllib import request
import  os
import urllib.error
import wget



def download(url,fname):

    html=request.urlopen(url)

    with open(fname,'wb') as fobj:

        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

def get_url(fname,patt,encoding):
    url_list=[]
    cpatt=re.compile(patt)

    with open(fname,encoding) as fobj:

        for line in fobj:

            for m in cpatt.finditer(line):
                url_list.append(m.group())

        return url_list


if __name__ == '__main__':
    net_url='http://www.tmooc.cn/'
    fname='/zxw/Python/stage3/day04/tmooc.html'
    url_patt='http://[\w./-]+ \.(jpg|png|jpeg|gif)'
    #download(net_url,fname)
    wget.download(net_url,fname)

    url_list=get_url(fname,url_patt,'r')

    print(url_list)

    folder= '/zxw/Python/stage3/day04/picture/'
    if not os.path.exists(folder):

        os.mkdir(folder)
        for url in url_list:
            fname = url.split('/')[-1]
            fname=os.path.join(folder,fname)
        try:
            download(url,fname)
        except urllib.error.HTTPEorr:
            print(url)