#-*-coding:utf-8-*-
import  pymysql          #pymysql

conn =pymysql.connect(
    host = '127.0.0.1',
    port=3306,
    user='root',
    passwd='123qqq...A',
    db='nsd1808',
    charset='utf8'
)
cursor=conn.cursor()

# employees：工号、姓名、性别、部门ID、email、出生日期
create_dep=''' create table departments(
dep_id int, 
dep_name varchar(20) not null UNIQUE , 
primary key(dep_id)
)
'''
cursor.execute(create_dep)


# departments：部门ID、部门名
create_employees=""" create table employees(
emp_id int,
emp_name varchar(20) not null UNIQUE,
gender varchar(6),
birth_date DATE,
email varchar(50),
dep_id int,
primary key(emp_id),
foreign key(emp_id) REFERENCES departments(dep_id)
)
"""
cursor.execute(create_employees)


# salary：工资日、工号、基本工资、奖金
create_salary=''' create table salary(
auto_id int,
date DATE,
emp_id int,
basic int,
awards int,
primary key(auto_id),
FOREIGN KEY(auto_id) REFERENCES employees(emp_id)
)
'''
cursor.execute(create_salary)


cursor.close()
conn.close()