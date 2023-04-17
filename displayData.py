import mysql.connector as c

con = c.connect(host='localhost', user='root', passwd='mysql', database='mysql')
cursor = con.cursor()

query = "SELECT * FROM students"
cursor.execute(query)

# data = cursor.fetchone()
# print(data)

# data2 = cursor.fetchmany(2)
# print(data2)

data3 = cursor.fetchall()
print(data3)
