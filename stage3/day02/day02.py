#-*-coding:utf-8-*-
#1)
#安装mariadb
#设置密码

#
#2)利用python模块对数据库进行基本操作
#安装python的pyMysql模块

#cd /mnt/zzg_pypkgs/pymysql_pkgs/
#pip3 install *

################################
#1)连接具体的数据库

# import pymysql
#
# conn = pymysql.connect(
#     host='127.0.0.1',
#
# )
#
#
# #2)游标 #取数据,像指针一样
# cursor=conn.cursor()
#
#
# #3)如何利用pymysql建表
# # employees：工号、姓名、性别、部门ID、email、出生日期
#
# create_dep=''' create table departments(
# dep_id int,
# dep_name varchar(20) not null UNIQUE ,
# primary key(dep_id)
# )
# '''
# cursor.execute(create_dep)
# #字符串里是执行的sql命令-->通过新的cursor连接上nsd1808后执行sql命令
#
#
# #4)
# cursor.close(4)
# #读完关闭
# conn.close()
# #执行完断开连接
#
# #5)连接插入数据
# #import  pymysql
# #conn=pymysql.connect()
# #cursor=cnn.cursor()
# insert1='insert into departments values(%s, %s)'
# cursor.execute(insert1,(1,'HR'))
# #执行insert1查询语句,传递参数-->1 int ,'HR'
#
# deps=[(2,'aa'),(3,'bb'),(4,'cc')]
# cursor.executemany(insert1,deps)
# #参数可以一个列表,多个元组数据元素.执行多个插入操作
#
# conn.commit()
# #对表修改需要提交,就像事务一样
#
# #5)查询数据
# sql='select * from department '
# cursor.execute(sql)
# #将执行结果标识
#
# result=cursor.fetchone()#取出一个
# print(result)
#
# result=cursor.fetchmany(3) #取出接下来三个
# print(result)
#
# result=cursor.fetchall()  #取出最后三个
# print(result)
#
#
# #移动游标
# sql1='select * from department'
# cursor.execute(sql1)
# cursor.scroll(1,mode='absolute')
# print (cursor.fetchone())
# cursor.scroll(2,mode='relative')
# print(cursor.fetchall())
# #可以先将游标移动到自己想要的
# #然后然后取出剩下数据
#
#
# #6)修改数据
# sql='update departments set dep_name=%s where dep_name=%s'
# cursor.execute(sql,(1,'kk')
# conn.commit()
#
# #7)删除数据s
# sql='delete from'
# conn.commit()

####################################################

#2.利用sqlalchemy来对数据库管理
#提供 SQL 具包及对象关系映 射(ORM) 工具
#采用简单的Python语言,为高效和高性能的数据库访问设计
#目标是提供能兼容众多数据库(如 SQLite、MySQL、Postgresql、Oracle、MS-SQL、SQLServer 和
#Firebird)的企业级持久性模型

# ORM即对象关系映射

# 数据库表是一个二维表,包含多行多列。把一个表的
# 内容用Python的数据结构表示出来的话,可以用一
# 个list表示多行,list的每一个元素是tuple,表示一行
# 记录

#安装sqlalchemy模块
#cd /mnt/zzg_pypkgs/sqlalchemy_pkgs
#pip3 install  sqlalchemy_pkgs

#1)engine连接数据库
#
# from sqlalchemy import create_engine
# #调用引擎模块
#
# engine=create_engine('mysql+pymysql://root:tedu.cn@localhost/\
# tarena',encoding='utf8',echo=True)
# #建立连接







#
# 6)
#
#
# 3)sqlalchemy安装


