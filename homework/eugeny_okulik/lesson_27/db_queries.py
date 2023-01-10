import mysql.connector as mysql


db = mysql.connect(
   host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
   port=25060,
   user='user1',
   passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
   database='qap09'
)

cursor = db.cursor(dictionary=True)
# cursor.execute('select * from students')
# cursor.execute('select * from students WHERE id = 2')
# result = cursor.fetchall()
# result = cursor.fetchone()
# print(result['name'])
# for row in result:
#     print(row['name'])

query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
# query = 'INSERT INTO students (name, surname) VALUES ({0}, {1})'
cursor.execute(query, ('Misha', 'Vasin'))
db.commit()
query_id = cursor.lastrowid
print(query_id)


db.close()
