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
group_values = ('AQA_Python', '2022-09-15', '2023-02-13')
cursor.execute(add_group_query, group_values)
db.commit()
add_group_query_id = cursor.lastrowid

add_student_query = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
student_values = ('Alesya', 'Kurylenka', add_group_query_id)
cursor.execute(add_student_query, student_values)
db.commit()
add_student_query_id = cursor.lastrowid

add_two_books_query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
books_values = [
    ('Three Comrades', add_student_query_id),
    ('Arch of Triumph', add_student_query_id)
]
cursor.executemany(add_two_books_query, books_values)
db.commit()

get_student_data_query = f"""
SELECT s.id, s.name, s.second_name, g.title as group_title, b.title as book_title
FROM students s
JOIN books b JOIN `groups` g
ON s.id = b.taken_by_student_id AND s.group_id = g.id
WHERE s.id = {add_student_query_id}
"""
cursor.execute(get_student_data_query)
data_result = cursor.fetchall()
books_list = [book['book_title'] for book in data_result]
print(f'''Student {data_result[0]['name']} {data_result[0]['second_name']} \
studies in the {data_result[0]['group_title']} group \
and took in the library the following books: {", ".join(books_list)}''')

db.close()
