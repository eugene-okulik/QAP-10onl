SELECT * FROM students
SELECT * FROM students WHERE group_id = 1 LIMIT 1

select * FROM books where title = 'Python for dummies' and taken_by_student_id  = 2
SELECT  end_date, title FROM `groups`


-- UPDATE students SET name = 'Petr',  second_name = 'Petrov' WHERE id = 9

INSERT INTO students VALUES (4, 'Jeorge', 'Washington', 3)
INSERT INTO students (name, second_name) VALUES ('Bill', 'Clinton')
INSERT INTO books (title, taken_by_student_id) SELECT title, taken_by_student_id FROM books WHERE title ='Finansist'
SELECT * FROM books WHERE title ='Finansist'

-- DELETE FROM books WHERE taken_by_student_id = 4

SELECT * FROM books WHERE id >= 1 ORDER BY title DESC 
SELECT * FROM books WHERE taken_by_student_id is NULL

SELECT s.name, s.second_name, b.title as book_title, s.id 
FROM students s 
JOIN books b 
ON s.id = b.taken_by_student_id 
WHERE s.second_name = 'Jackson'

SELECT s.name, s.second_name, b.title as book_title, s.id 
FROM students s 
LEFT JOIN books b 
ON s.id = b.taken_by_student_id 

SELECT s.name, s.second_name, b.title as book_title, s.id 
FROM students s 
RIGHT JOIN books b 
ON s.id = b.taken_by_student_id 
