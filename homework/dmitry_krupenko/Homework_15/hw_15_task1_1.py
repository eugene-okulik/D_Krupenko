# использовал pymysql потому что ловил Process finished with exit code -1073741819 (0xC0000005)
# при использовании mysql-connector,as а на pymysql отрабатывает без проблем
import pymysql as mysql

db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    database='st-onl'
)

cursor = db.cursor()

cursor.execute(
    'INSERT INTO students (name, second_name) VALUES (%s, %s)',
    ('Dazdranagon2', 'Utesov')
)
db.commit()

student_id = cursor.lastrowid

print('student_id:', student_id)

cursor.execute(
    'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)',
    ('moms_aqa', '2026-03-11', '2027-04-10')
)
db.commit()

group_id = cursor.lastrowid

print('group_id:', group_id)

cursor.execute(
    'UPDATE students SET group_id = %s WHERE id = %s',
    (group_id, student_id)
)
db.commit()

books = ['book_any1', 'book_any2', 'book_any3']
cursor.executemany(
    'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)',
    [(book, student_id) for book in books]
)
db.commit()

subjects = ['flying', 'lying', 'riding']
subject_ids = []

for subject in subjects:
    cursor.execute(
        'INSERT INTO subjects (title) VALUES (%s)',
        (subject,)
    )
    subject_ids.append(cursor.lastrowid)

db.commit()

print('subject_ids:', subject_ids)

lessons_titles = {
    subject_ids[0]: ['any_value', 'any_any2'],
    subject_ids[1]: ['something', 'anything'],
    subject_ids[2]: ['somewhere', 'anywhere']
}

lesson_ids = []

query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'

for subject_id, lessons in lessons_titles.items():
    for lesson in lessons:
        cursor.execute(query, (lesson, subject_id))
        lesson_ids.append(cursor.lastrowid)

db.commit()

print('lesson_ids:', lesson_ids)

marks = [1, 2, 3, 4, 5, 6]

data = [
    (student_id, lesson_id, mark)
    for lesson_id, mark in zip(lesson_ids, marks)
]

cursor.executemany(
    'INSERT INTO marks (student_id, lesson_id, value) VALUES (%s, %s, %s)',
    data
)

db.commit()

cursor.execute(
    'SELECT value FROM marks WHERE student_id = %s',
    (student_id)
)
print('student_marks:', [row[0] for row in cursor.fetchall()])

cursor.execute(
    'SELECT title FROM books WHERE taken_by_student_id = %s',
    (student_id)
)
print('books:', [row[0] for row in cursor.fetchall()])
cursor.execute("""
SELECT
s.name,
s.second_name,
g.title group_name,
b.title book,
l.title lesson,
sub.title subject,
m.value mark
FROM students s
Left JOIN `groups` g ON g.id = s.group_id
Left JOIN books b ON b.taken_by_student_id = s.id
Left JOIN marks m ON m.student_id = s.id
Left JOIN lessons l ON l.id = m.lesson_id
Left JOIN subjects sub ON sub.id = l.subject_id
WHERE s.id = %s
""", (student_id,))
rows = cursor.fetchall()

print('All data:')

for name, second_name, group, book, lesson, subject, mark in rows:
    print(
        f'Name: {name}, Second name: {second_name}, Group: {group}, Book: {book}, '
        f'Lesson: {lesson}, Subject: {subject}, Mark: {mark}'
    )

cursor.close()
db.close()
