import sqlite3
from unittest import result
conn=sqlite3.connect("lib_project",isolation_level=None)

c=conn.cursor()

c.execute("INSERT INTO userlist VALUES('qaz','승렬','111111',NULL,NULL,NULL)")
c.execute("INSERT INTO userlist VALUES('wsx','근영','222222',NULL,NULL,NULL)")
c.execute("INSERT INTO userlist VALUES('edc','명석','333333',NULL,NULL,NULL)")


sql = "select * from userlist"
c.execute(sql)
result = c.fetchall()
print(result)
c.close()
