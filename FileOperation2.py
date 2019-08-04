import mysql.connector

connection = mysql.connector.connect(host='localhost', database='myorg', user='admin', passwd='novell')
mycurser = connection.cursor()
mycurser.execute("select * from student")

result = mycurser.fetchone()

for i in mycurser:
    print(i)