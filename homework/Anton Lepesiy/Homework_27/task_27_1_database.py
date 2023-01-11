import mysql.connector as mysql


db = mysql.connect(
    host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
    database='qap09'
)

cursor = db.cursor(dictionary=True)

group_create = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
group_parameters = ('GDA-23', '2021-11-17', '2023-12-31')
cursor.execute(group_create, group_parameters)
db.commit()
new_group_id = cursor.lastrowid

add_new_student = 'INSERT INTO `students` (name, second_name, group_id) VALUES (%s, %s, %s)'
new_student = ('Marti', 'McFly', new_group_id)
cursor.execute(add_new_student, new_student)
db.commit()
student_id = cursor.lastrowid

add_a_book = 'INSERT INTO `books` (title, taken_by_student_id) VALUES (%s, %s)'
books = [
        ('Lucky Star', student_id),
        ('Dune', student_id)
        ]
cursor.executemany(add_a_book, books)
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
       f'and took the following books from the library:  {", ".join(student_books)}'
print(text)
