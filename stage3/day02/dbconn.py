#-*-coding:utf-8-*-

from sqlalchemy import  create_engine     #引擎模块
from sqlalchemy.ext.declarative import declarative_base #自定义基类模块
from sqlalchemy import  Column, Integer,String,ForeignKey,Date
from sqlalchemy.orm import sessionmaker   #访问数据库

engine= create_engine(
    'mysql+pymysql://root:123qqq...A@127.0.0.1/tedu1808?charset=utf8',
    encoding='utf8'
    #echo=True
)   #连接数据库

Session =sessionmaker(bind=engine)                   #绑定引擎连接数据库,然后访问数据库

Base =declarative_base()                             #创建基类也就是父类
class Department(Base):                              #基于父类的子类
    __tablename__='departments'                      #表名
    dep_id = Column(Integer,primary_key=True)        #表字段
    dep_name=Column(String(20),nullable=False,unique=True)

    def __str__(self):
        return "<部门: %s>" % self.dep_name           #打印的时候返回值

class Employees(Base):                               #
    __tablename__='employees'
    emp_id=Column(Integer,primary_key=True)
    emp_name=Column(String(20))
    email=Column(String(20))
    dep_id=Column(Integer,ForeignKey('departments.dep_id'))

    def __str__(self):
        return "<姓名: %s>" %self.emp_name

class Salary(Base):
    __tablename__='salary'
    auto_id=Column(Integer,primary_key=True)
    date=Column(Date)
    emp_id=Column(Integer,ForeignKey('employees.emp_id'))
    basic=Column(Integer)
    awards=Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)  #通过表的映射类,在数据库创建表
