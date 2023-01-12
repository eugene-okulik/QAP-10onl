import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
    database='qap09'
)

cursor = db.cursor(dictionary=True)

add_group_sql = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
group_args = ('QAP10', '2022-09-15', '2023-02-13')
cursor.execute(add_group_sql, group_args)
db.commit()
group_id = cursor.lastrowid

add_student_sql = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
student_args = ('Dmitry', 'Gorski', f'{group_id}')
cursor.execute(add_student_sql, student_args)
db.commit()
student_id = cursor.lastrowid

add_books_sql = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
books = [('Python Crash Course', f'{student_id}'), ('Python Pocket Reference', f'{student_id}')]
cursor.executemany(add_books_sql, books)
db.commit()

get_student_data_sql = f"""
SELECT name, second_name, g.title as group_title, b.title as book_title from `groups` g 
JOIN students s on g.id = s.group_id
JOIN books b on b.taken_by_student_id = s.id
WHERE s.id = {student_id}
"""

cursor.execute(get_student_data_sql)
students_info = cursor.fetchall()
books = ', '.join([books['book_title'] for books in students_info])

print(
    f"Student {students_info[0]['name']} {students_info[0]['second_name']} "
    f"studies in the {students_info[0]['group_title']} and took in the library the following books: {books}")

db.close()
