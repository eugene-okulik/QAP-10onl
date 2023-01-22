import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-64949-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='AVNS_CBt-mC3cbjNrlcTNBr_',
    database='qap09'
)

group_id = 'GROUP_1001001'
name = 'Perry'
second_name = 'Cox'

cursor = db.cursor(dictionary=True)
cursor.execute("insert into `groups` (title, start_date, end_date) "
               f"values ('{group_id}', '2022-01-01', '2025-01-01' )")
cursor.execute("select max(id) as id from  `groups` "
               f"where title = '{group_id}' ")
cursor.execute("insert into students (name, second_name, group_id)"
               f"values ('{name}', '{second_name}', {cursor.fetchone()['id']})")
cursor.execute("select max(id) as id from students "
               f"where group_id in (select max(id) from `groups` where title = '{group_id}')")
student_id = cursor.fetchone()['id']
cursor.execute(f"insert into books(title,taken_by_student_id) values('Book for Perry 1', {student_id})")
cursor.execute(f"insert into books(title,taken_by_student_id) values('Book for Perry 2', {student_id})")
db.commit()

cursor.execute("select s.name, s.second_name, g.title as group_title, b.title as book_title "
               "from `groups` g inner join students s on g.id = s.group_id "
               "inner join books b on s.id = b.taken_by_student_id "
               f"where s.id in (select max(id) from students where name = '{name}' and second_name = '{second_name}')")

request_result = cursor.fetchall()
final_result = {}
for i in range(len(request_result)):
    for k, v in request_result[i].items():
        if k == 'book_title':
            final_result[k + str(i)] = v
        else:
            final_result[k] = v

print(f"Студент {final_result['name']} {final_result['second_name']} учится в группе {final_result['group_title']} "
      f"и взял в библиотеке следующие книги: {final_result['book_title0']}, {final_result['book_title1']}")
db.close()
