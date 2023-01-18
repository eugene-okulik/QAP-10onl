import mysql.connector as mysql


db = mysql.connect(
    host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
    database='qap09'
)

cursor = db.cursor(dictionary=True)
add_group = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
group_values = ('QAP-10onl', '2023-01-01', '2023-02-02')
cursor.execute(add_group, group_values)
db.commit()
group_id = cursor.lastrowid

add_student = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
student_values = ('Elena', 'Rybina', group_id)
cursor.execute(add_student, student_values)
db.commit()
student_id = cursor.lastrowid

add_books = 'INSERT INTO `books` (title, taken_by_student_id) VALUES (%s, %s)'
books = [
    ('Harry Potter', student_id),
    ('Don Quixote', student_id)
]
cursor.executemany(add_books, books)
db.commit()

student_info = 'SELECT s.name, s.second_name, b.title as book_title, s.id, g.title as group_name ' \
               'FROM `students` s ' \
               'JOIN `books` b ' \
               'ON s.id = b.taken_by_student_id ' \
               'JOIN `groups` g ' \
               'ON g.id = s.group_id ' \
               f'WHERE s.id  = {student_id}'
cursor.execute(student_info)
result = cursor.fetchall()
student_name = result[0]['name']
student_surname = result[0]['second_name']
group_name = result[0]['group_name']
student_books = []
for row in result:
    student_books.append(row['book_title'])
db.close()

text = f'Student {student_name} {student_surname} studies in group {group_name} ' \
       f'and took in the library the following books:  {", ".join(student_books)}'
print(text)
