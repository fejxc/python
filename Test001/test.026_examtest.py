import pymysql
import mysql.connector
#要导入连接器 不然不能连接
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="061100sy",db="student")
conn2=pymysql.connect(host="127.0.0.1",user="root",passwd="061100sy",db="student")
# print(conn)
sql="select * from users"
sql2="select * from mess"
cur=conn.cursor()
cur.execute(sql)
cur2=conn.cursor()
cur2.execute(sql2)
for value in cur:
    print('姓名'+value[1]+'  '+'密码'+value[2])
conn.close()
for value in cur2:
    print('姓名'+str(value[0])+'  '+'学号'+str(value[1]))
conn2.close()