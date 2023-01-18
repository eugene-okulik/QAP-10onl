import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
    database='qap09'
)

cursor = db.cursor(dictionary=True)

query_create_group = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
group_value = ('QAP-10', '2022-01-10', '2023-01-10')
cursor.execute(query_create_group, group_value)
query_create_group_id = cursor.lastrowid

query_create_student = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
student_value = ('Konstantin', 'Ibragimov', query_create_group_id)
cursor.execute(query_create_student, student_value)
query_create_student_id = cursor.lastrowid

query_create_book = 'INSERT INTO books (title, taken_by_student_id)  VALUES (%s, %s)'
book_value = [
    ('Learning Python (part 1)', query_create_student_id),
    ('Learning Python (part 2)', query_create_student_id)
]
cursor.executemany(query_create_book, book_value)

db.commit()

query_result = f'''
SELECT s.name as first_name, s.second_name as second_name, g.title as group_title, b.title as book_title
FROM students s
JOIN books b
JOIN `groups` g
ON s.id = b.taken_by_student_id
AND s.group_id  = g.id
WHERE s.group_id = {query_create_group_id}
'''
cursor.execute(query_result)
result = cursor.fetchall()
print(f'''Student {result[0]['first_name']} {result[0]['second_name']} \
study in {result[0]['group_title']} group and took from library the following books: \
"{result[0]['book_title']}", "{result[1]['book_title']}".'''
      )

db.close()
