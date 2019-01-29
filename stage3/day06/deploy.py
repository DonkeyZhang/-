#-*-coding:utf-8-*-
import wget
import os
import requests
import hashlib
import tarfile

def has_new_version(live_url, live_fname):

    if not os.path.isfile(live_fname):  #版本文件不存在就没有新版本
        return True

    with open(live_fname) as fobj:     #存在的话读取本地的最新版本文件
        local_version=fobj.read()

    r = requests.get(live_url)         #读取jenkins服务端的最新版本文件
    if r.text !=local_version:
        return True

    return False                       #返回Fasle 就代表是最新文件


def md5sum(fname):
    m=hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data=fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

############################

def deploy(app_fname,deploy_dir):

    os.chdir(deploy_dir)                #切换目录
    tar=tarfile.open(app_fname,'r:gz')  #在目录下打开最新的网页
    tar.extractall()                    #全部解压到部署目录下
    tar.close()

    app_path=os.path.basename(app_fname)       #取出tar名
    app_path=app_fname.replace('.tar.gz','')   #去掉后缀变成文件夹
    app_path=os.path.join(deploy_dir,app_path) #将/var/www/deploy+myweb_1.0

    dest_path = '/var/www/html/nsd1808'        #目标文件夹
    if os.path.exists(dest_path):              #先查看目标文件夹存不存在
        os.unlink(dest_path)                   # 存在就是先删除连接
    os.symlink(app_path,dest_path)             #建立链接,保证两文件内容相同


if __name__ == '__main__':
# 1、判断是否有最新版本
# 2、如果有新版本则下载
# 3、判断下载的软件包是否是完整的
# 4、如果软件包完整，则解压缩并部署


#判断是否有最新版本
#/var/www/-->建deploy/download/ 和 /var/www/html/ --->建nsd1808

    live_url='http://192.168.4.3/deploy/live_version'      #更新的最新本版放在live_version
    live_fname = '/var/www/deploy/live_version'            #真机web服务器,本地的最新版本

    if not has_new_version(live_url,live_fname):           #调用has_new_version判断
        print('没有新本版')
        exit()

###如果有新版本则下载

    r=requests.get(live_url)                          #读取最新的版本号
    download_dir='/var/www/download'                  #本地放下载的tar包的地方
    deploy_dir='/var/www/deploy'                      #本地部署部署网页放的地方-->做硬链接到/html

    app_url='http://192.168.4.3/deploy/packages/myweb_%s.tar.gz' % (r.text.strip())

    #最新版本的下载地址--->jenkins

    wget.download(app_url,download_dir)

    #下载最新版本的网页到到下载目录

#判断下载的软件包是否是完整的

    app_md5_url=app_url + '.md5'
    #最新版本美的 md5的文件下载地址
    wget.download(app_md5_url,download_dir)
    #下载md5文件地址到下载目录


    if os.path.exists(live_fname):     #如果要更新网页了,老版本的版本文件需要删除
        os.remove(live_fname)
    wget.download(live_url,deploy_dir) # 再下载最新版本的文件

    app_fname=os.path.join(download_dir,app_url.split('/')[-1])
    #下载的网页的绝对路径-->tar包放的地方

    local_md5=md5sum(app_fname)  #得到本地文件的md5值
    r=requests.get(app_md5_url)  #jenkins服务端md5的值

    if local_md5!=r.text.strip():#判断有没有下载成功
        print('文件校验失败')
        exit(1)

    deploy(app_fname,deploy_dir) #成功后部署网页
