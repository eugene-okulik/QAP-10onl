import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
    database='qap09'
)

cursor = db.cursor(dictionary=True)

add_group_query = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
cursor.execute(add_group_query, ('New Group', '2022-12-12', '2023-12-12'))
db.commit()
group_id = cursor.lastrowid

add_student_query = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
cursor.execute(add_student_query, ('Юрий', 'Перекатиполе', group_id))
db.commit()
student_id = cursor.lastrowid

add_books_query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
books = [
    ('Зов Ктулху', student_id),
    ('Хребты безумия', student_id)
]
cursor.executemany(add_books_query, books)
db.commit()

summary_query = 'SELECT s.name, s.second_name, s.group_id, b.title as book_title, s.id ' \
                'FROM students s ' \
                'JOIN books b ' \
                'ON s.id = b.taken_by_student_id ' \
                f'WHERE s.id  = {student_id}'
cursor.execute(summary_query)
summary = cursor.fetchall()
student_name = summary[0]['name']
student_second_name = summary[0]['second_name']
student_group = summary[0]['group_id']
student_books = []
for i in summary:
    student_books.append(i['book_title'])

print(f'Student {student_name} {student_second_name} study in {student_group} group and took in the'
      f'library books: {student_books}')
db.close()
