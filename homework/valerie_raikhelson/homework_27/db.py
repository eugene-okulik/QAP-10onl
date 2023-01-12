import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
    database='qap09'
)

create_group_query = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
create_student_query = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
create_book_query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'

cursor = db.cursor(dictionary=True)

group = ('GPN-001', '2023-01-01', '2023-12-12')
cursor.execute(create_group_query, group)
group_id = cursor.lastrowid
db.commit()

student = ('Ivan', 'Ivanov', group_id)
cursor.execute(create_student_query, student)
student_id = cursor.lastrowid
db.commit()

books = [('SQL', student_id), ('Python', student_id)]
cursor.executemany(create_book_query, books)

get_student = f"""
SELECT s.name,
       s.second_name,
       g.title AS group_title,
       b.title AS book_title
FROM students  s JOIN books  b JOIN `groups` g 
ON s.id  = b.taken_by_student_id AND s.group_id  = g.id
WHERE s.id  = {student_id} """

cursor.execute(get_student)
result = cursor.fetchall()
print(f'''Student {result[0]['name']} {result[0]['second_name']} \
studied in the {result[0]['group_title']} group and took possible books from the library: \
"{result[0]['book_title']}", "{result[1]['book_title']}".'''
      )

db.close()
