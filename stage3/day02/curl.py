#-*-coding:utf-8-*-
import  pymysql
conn=pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123qqq...A',
    db='nsd1808',
    charset='utf8'
)

cursor = conn.cursor()

# insert1 ='insert into departments values( %s,%s)'
#
# cursor.execute(insert1,(1,'HR'))
#
# deps = [(2, '运维'), (3, '开发'), (4, '测试')]
# cursor.executemany(insert1, deps)
#
# deps2 = [(5, '行政'), (6, '财务'), (7, '市场')]
# cursor.executemany(insert1, deps2)
#
# conn.commit()



# query1 = ' select * from departments order by dep_id'
# cursor.execute(query1)
#
# result1=cursor.fetchone()
# print(result1)
# print('*' * 30)
#
# result2=cursor.fetchmany(3)
# print(result2)
# print('*' * 30)
#
# result3=cursor.fetchall()
# print(result3)

# (1, 'HR')
# ******************************
# ((2, '运维'), (3, '开发'), (4, '测试'))
# ******************************
# ((5, '行政'), (6, '财务'), (7, '市场'))
################################################

# query1 = ' select * from departments order by dep_id'
# cursor.execute(query1)
#
# cursor.scroll(1,mode='absolute')
# print(cursor.fetchone())
#
# cursor.scroll(2,mode='relative')
# print(cursor.fetchone())

#
# (2, '运维')
# (5, '行政'
############################################################
# update = 'update  departments set dep_name=%s WHERE  dep_name=%s'
# cursor.execute(update,('人事部','HR'))
# conn.commit()
#############
delete1 = 'delete form departments  where dep_id =%s'
cursor.execute(delete1,(7,))
conn.commit()





cursor.close()
conn.close()