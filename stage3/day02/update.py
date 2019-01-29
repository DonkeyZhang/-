#-*-coding:utf-8-*-
from dbconn import Department ,Session

session =Session()
# sales =Department(dep_id=6, dep_name='销售')
# session.add(sales)
# session.commit()
######################################

# xs=session.query(Department).filter(Department.dep_id==6)
# xs=xs.one()
# print(xs)
# xs.dep_name='销售部'
# session.commit()
########################################

# xs=session.query(Department).filter(Department.dep_id==6)
# xs=xs.one()
# xs.delete(xs)
# xs.commit()