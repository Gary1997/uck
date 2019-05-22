import pymysql
host = '127.0.0.1'
port = 8080
user = 'root'
password = 123456
databse = 'stu'
charset = 'utf8'
db = pymysql.connect(host,port,user,password,databse,charset)
c= db.class_1
print(c)