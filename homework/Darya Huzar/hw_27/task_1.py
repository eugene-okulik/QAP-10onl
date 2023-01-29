import mysql.connector as mysql


db = mysql.connect(
    host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
    database='qap09'
)

cursor = db.cursor(dictionary=True)

group_data = ('QAP-10onl', '2022-09-15', '2023-02-13')
cursor.execute('INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)', group_data)
db.commit()
id_gr = cursor.lastrowid

student = ('Darya', 'Huzar', id_gr)
cursor.execute('INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)', student)
db.commit()
id_st = cursor.lastrowid

book_list = [('Pride and Prejudice', id_st),
             ('The great Gatsby', id_st)]
cursor.executemany('INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)', book_list)
db.commit()

cursor.execute(f'SELECT s.name, s.second_name, g.title as gr_title, b.title as book_title from `groups` g '
               f'JOIN students s ON s.group_id = g.id JOIN books b ON s.id = b.taken_by_student_id '
               f'WHERE s.id = {id_st}')
results = cursor.fetchall()
if not results:
    print('There is not result of your query.')
else:
    my_list = [res.get('book_title', 'No book') for res in results]
    name = results[0].get('name', 'No name')
    second_name = results[0].get('second_name', 'No second_name')
    gr_name = results[0].get('gr_title', 'No group_name')
    print(f"Student {name} {second_name} studies in {gr_name} group and "
          f"has taken the following books: {', '.join(my_list)} at the library.")
db.close()
