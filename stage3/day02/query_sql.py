#-*-coding:utf-8-*-
from dbconn import  Department,Employees,Session

session=Session()

# query1=session.query(Department)       #查询表Department

# print(query1)                          #返回查询语句本身
# print('*' * 30 )
#

# print(query1.all())                    #返回所有对象
# print('*' * 30)
#

# for dep in query1:                     #打印每一条实例返回 __str__ 里的方法
#     print(dep)
# print('*' * 30)
#
# for dep in query1:                     #打印每一条具体实例的每一具体具体属性
#     print('%s %s' % (dep.dep_id,dep.dep_name))



# SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name
# FROM departments
# ******************************
# [<dbconn.Department object at 0x7f966854f828>, <dbconn.Department object at 0x7f966854f198>, <dbconn.Department object at 0x7f966854f5c0>, <dbconn.Department object at 0x7f966854f6a0>, <dbconn.Department object at 0x7f966854f518>]
# ******************************
# <部门: HR>
# <部门: 开发部>
# <部门: 测试部>
# <部门: 财务部>
# <部门: 运维部>
# ******************************
# 1 HR
# 3 开发部
# 4 测试部
# 5 财务部
# 2 运维部
#######################################

# query2=session.query(Employees.emp_name,Employees.email)
#
# print(query2)
# print('*' * 30)
#
# print(query2.all())
# print('*' * 30)
#
# for name, email in query2:
#     print('%s: %s' % (name,email))

# SELECT employees.emp_name AS employees_emp_name, employees.email AS employees_email
# FROM employees
# ******************************
# [('田超', 'tc@qq.com'), ('白宇', 'by@qq.com'), ('白尚松', 'bss@163.com'), ('何东阳', 'hdy@163.com'), ('房果', 'fg@qq.com'), ('巫菲红', 'wfh@tedu.com'), ('冯翠雯', 'fcw@tarena.com'), ('孙正', 'sz@126.com'), ('章勤浩', 'zqh@126.com'), ('陈佳乐', 'cjl@qq.com'), ('黄平武', 'hpw@163.com'), ('柏宏', 'bh@qq.com'), ('唐瑞', 'tr@qq.com'), ('鲁俊', 'lj@qq.com')]
# ******************************
# 田超: tc@qq.com
# 白宇: by@qq.com
# 白尚松: bss@163.com
# 何东阳: hdy@163.com
# 房果: fg@qq.com
# 巫菲红: wfh@tedu.com
# 冯翠雯: fcw@tarena.com
# 孙正: sz@126.com
# 章勤浩: zqh@126.com
# 陈佳乐: cjl@qq.com
# 黄平武: hpw@163.com
# 柏宏: bh@qq.com
# 唐瑞: tr@qq.com
# 鲁俊: lj@qq.com

#############################################

# query3 = session.query(Department.dep_name.label('部门'))
# print(query3)
#
# print(query3.all())
#
#
# for dep in query3:
#         print(dep.部门)


# SELECT departments.dep_name AS `部门`
# FROM departments


# [('HR',), ('开发部',), ('测试部',), ('财务部',), ('运维部',)]
# HR
# 开发部
# 测试部
# 财务部
# 运维部

#####################################################

# query4 = session.query(Department).order_by(Department.dep_id)
# print(query4)
#
# for dep in query4:
#     print('%s: %s' % (dep.dep_id,dep.dep_name))
# SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name
# FROM departments ORDER BY departments.dep_id
# 1: HR
# 2: 运维部
# 3: 开发部
# 4: 测试部
# 5: 财务部

###############################################################
# query5 =session.query(Department).order_by(Department.dep_id)[1:3]
# print(query5)
#
# for dep in query5:
#     print('%s: %s' % (dep.dep_id,dep.dep_name))
#
# [<dbconn.Department object at 0x7f6f53c227f0>, <dbconn.Department object at 0x7f6f53c22908>]
# 2: 运维部
# 3: 开发部
###########################################
# query6=session.query(Department).filter(Department.dep_id==3)
# print(query6)
#
# for dep in query6:
#     print('%s %s' % (dep.dep_id,dep.dep_name))
#
# SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name
# FROM departments
# WHERE departments.dep_id = %(dep_id_1)s
# 3 开发部

#################################

# quer7=session.query(Employees.emp_name,Employees.email).filter(Employees.dep_id==2)\
#     .filter(Employees.email.like('%@qq.com'))
# print(quer7)
#
# for name,email in quer7:
#     print('%s: %s' % (name, email))
#
# SELECT employees.emp_name AS employees_emp_name, employees.email AS employees_email
# FROM employees
# WHERE employees.dep_id = %(dep_id_1)s AND employees.email LIKE %(email_1)s
# 白宇: by@qq.com
# 房果: fg@qq.com
# 柏宏: bh@qq.com

################################################################
# query8 =session.query(Employees.emp_name,Employees.email)\
#     .filter(Employees.emp_name.in_(['巫菲红','章勤浩']))
# print(query8)
#
# for name,email in query8:
#     print('%s: %s' % (name, email))

# SELECT employees.emp_name AS employees_emp_name, employees.email AS employees_email
# FROM employees
# WHERE employees.emp_name IN (%(emp_name_1)s, %(emp_name_2)s)
# 巫菲红: wfh@tedu.com
# 章勤浩: zqh@126.com

############################
# query9 =session.query(Employees.emp_name,Employees.email)\
#     .filter(~Employees.emp_name.in_(['巫菲红','章勤浩']))
# print(query9)
#
# for name,email in query9:
#     print('%s: %s' % (name, email))
#
# SELECT employees.emp_name AS employees_emp_name, employees.email AS employees_email
# FROM employees
# WHERE employees.emp_name NOT IN (%(emp_name_1)s, %(emp_name_2)s)
# 田超: tc@qq.com
# 白宇: by@qq.com
# 白尚松: bss@163.com
# 何东阳: hdy@163.com
# 房果: fg@qq.com
# 冯翠雯: fcw@tarena.com
# 孙正: sz@126.com
# 陈佳乐: cjl@qq.com
# 黄平武: hpw@163.com
# 柏宏: bh@qq.com
# 唐瑞: tr@qq.com
# 鲁俊: lj@qq.com
##############################################

# from sqlalchemy import  and_,or_
# query10=session.query(Employees.emp_name,Employees.email,Employees.dep_id)\
#     .filter(or_(Employees.dep_id==2,Employees.email.like('%@qq.com')))
# print(query10)
#
# for name,email,dep_id in query10:
#     print('%s: %s %s' % (name, email,dep_id))
#
# SELECT employees.emp_name AS employees_emp_name, employees.email AS employees_email, employees.dep_id AS employees_dep_id
# FROM employees
# WHERE employees.dep_id = %(dep_id_1)s OR employees.email LIKE %(email_1)s
# 田超: tc@qq.com 1
# 白宇: by@qq.com 2
# 白尚松: bss@163.com 2
# 房果: fg@qq.com 2
# 孙正: sz@126.com 2
# 陈佳乐: cjl@qq.com 5
# 柏宏: bh@qq.com 2
# 唐瑞: tr@qq.com 5
# 鲁俊: lj@qq.com 3
############################################################

# query11=session.query(Employees.emp_name,Employees.email)
# print(query11.first())
# #print(query11.all())[0]
#
# ('田超', 'tc@qq.com')

##################################################################

# query12=session.query(Employees.emp_name,Employees.email)\
#     .filter(Employees.emp_id==100)
# print(query12.one())
# print(query12.scalar())

# ('田超', 'tc@qq.com')
# 田超  #first Cloumn
##################################

# query13=session.query(Employees).filter(Employees.dep_id==2)
# print(query13.count())
#
# 5

###################################################
# query14 =session.query(Employees.emp_name,Department.dep_name)\
#     .join(Department,Department.dep_id==Employees.dep_id)
# print(query14.all())

# [(100, 'HR'), (301, 'HR'), (201, '开发部'), (401, '开发部'), (900, '开发部'),
#  (302, '测试部'), (600, '测试部'), (500, '财务部'), (800, '财务部'), (101, '运维部'), (200, '运维部'),
#  (300, '运维部'), (400, '运维部'), (700, '运维部')]
#

#############################################
# query15 =session.query(Department.dep_name,Employees.emp_name)\
#     .join(Employees,Department.dep_id==Employees.dep_id)
# print(query15.all())

##############################################
