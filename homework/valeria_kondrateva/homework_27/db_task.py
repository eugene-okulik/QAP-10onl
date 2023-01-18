import mysql.connector as mysql


db = mysql.connect(
    host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
    database='qap09'
)

cursor = db.cursor(dictionary=True)
create_group = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
group_values = ('qap10', '2022-09-01', '2023-02-01')
cursor.execute(create_group, group_values)
group_id = cursor.lastrowid

create_student = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
student_values = ('Valeria', 'Kondrateva', group_id)
cursor.execute(create_student, student_values)
student_id = cursor.lastrowid

create_books = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
books_values = [
    ('harry potter', student_id),
    ('gone with the wind', student_id)
]
cursor.executemany(create_books, books_values)

db.commit()

student = '''SELECT s.name, s.second_name, b.title as book_title, g.title as group_title
FROM students s
JOIN books b
JOIN `groups` g
ON s.group_id = g.id
WHERE s.group_id = 245'''

cursor.execute(student)
result = cursor.fetchall()

print(f"Student {result[0]['name']} {result[0]['second_name']} study in {result[0]['group_title']} group and take "
      f"from the library {result[0]['book_title']}, {result[4]['book_title']} books.")

db.close()
