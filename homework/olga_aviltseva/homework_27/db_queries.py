import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
    database='qap09'
)

cursor = db.cursor(dictionary=True)

query = 'insert into `groups` (title, start_date, end_date) values (%s, %s, %s)'
cursor.execute(query, ('GR1', '2023-01-21', '2023-01-31'))
db.commit()
group_id = cursor.lastrowid

query = 'insert into students (name, second_name, group_id) values (%s, %s, %s)'
cursor.execute(query, ('Olga', 'Aviltseva', group_id))
db.commit()
student_id = cursor.lastrowid

query = 'insert into books (title, taken_by_student_id) values (%s, %s)'
values = [
    ('Misery', student_id),
    ('The Long Walk', student_id)
    ]
cursor.executemany(query, values)
db.commit()


query = f'''SELECT CONCAT('Student ',  s.name,  ' ',  s.second_name,  ' studies in group ',  g.title,  ' 
and took the following books: ',  GROUP_CONCAT(b.title)) as result_text
from students s
join books b join `groups` g
on s.id = b.taken_by_student_id and s.group_id = g.id
group by
s.id, s.name, s.second_name, g.title, b.taken_by_student_id
having s.id = {student_id}'''

cursor.execute(query)
result = cursor.fetchone()
print(result['result_text'])

db.close()
