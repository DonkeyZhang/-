#-*-coding:utf-8-*-
#备份程序:
#1.非交互运行
#2.两个功能,完全备份,增量备份
#3.完全备份
# (1)把整个目录打包
# (2)生成每个文件的md5值
# (3)确定备份文件名称security_full_20190121.tar.gz
#4.增量备份
# (1)计算当前目录每个文件md5值
# (2)取出前一天的文件md5值
# (3)找出需要备份的文件进行备份
# (4)更新md5文件

import  os
import hashlib
import tarfile
import  pickle
from time import strftime


def check_md5(fname):   #检查文件内容,生成md5值

    m=hashlib.md5()     #md5函数

    with open(fname,'rb') as fobj:   #以rb的形式打开文件
        while True:                  #以4096的形式读取文件
            data = fobj.read(4096)

            if not data:             #如果不等于4096 没有值则结束循环
                break

            m.update(data)           #每读一次更新md5值,全读完,md5值得出

    return m.hexdigest               #返回 md5值


def full_backup(src_dir, dst_dir, md5file):               #完全备份
    fname=os.path.basename(src_dir.rstrip('/'))           #备份的源目录去除'/',有斜杠代文件名也显示出来了
    fname='%s_full_%s.tar.gz' % (fname,strftime('%Y%m%d'))#目录名加上现在的年月日
    fname=os.path.join(dst_dir,fname)                     #加上目标目录,直接创建tar包名
    # >> > fname = os.path.basename('/root/test1/'.rstrip('/'))
    # >> > fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    # >> > fname = os.path.join('/root/test2', fname)
    # >> > fname
    # '/root/test2/test1_full_20190121.tar.gz'

    tar =tarfile.open(fname,'w:gz')           # 以写入的方式打开一个名为fname的tar包
    tar.add(src_dir)                          #将源目录放入tar包
    tar.close()                               # 关闭文件

##生成md5值

    md5dict = {}
    for  path ,folder, files in os.walk(src_dir): #返回1)正在处理的目录2)每层目录有几个子目录,3)本层有什么文件名

        for file in files:                        #for循环文件名
            key =os.path.join(path ,file)         #将每层的路径名和文件名和文件名连接
            md5dict[key]=check_md5(key)           #调用check_md5函数,将每个件md5一下添加的字典

    with open(md5file,'wb') as fobj:              #以写入的方式打开md5file
        pickle.dump(md5dict,fobj)                 #将字典的值写入


def incr_backup(src_dir,dst_dir, md5file):       #
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)

    with open(md5file,'rb') as fobj: #将已有的数据读出
        old_md5 =pickle.load(fobj)   #久的数据到处-->字典

    cur_md5 ={}                      # 所有的md5值,包括新增的
    for path ,folders,files in os.walk(src_dir): #

        for file in files:
            key=os.path.join(path,file)
            cur_md5[key]=check_md5(key)

    with open(md5file,'wb') as fobj:  #把原来数据清空,新的数据填上
        pickle.dump(cur_md5,fobj)

    tar = tarfile.open(fname,'w:gz')  #以写入的方式的打开tar包文件,不清空

    for key in cur_md5:
        if old_md5.get(key) != cur_md5[key]: #原来数据的md5的值与新的md5的值对比
            tar.add(key)                     #如果不一样将新的文件加入tar包
    tar.close()


if __name__ == '__main__':
    src_dir = '/root/test1'
    dst_dir = '/root/test2'
    md5file = '/root/md5.data'

    if strftime('%a') == 'Mon':               #如果是Mon全备
        full_backup(src_dir,dst_dir,md5file)
    else:
        incr_backup(src_dir,dst_dir,md5file)
