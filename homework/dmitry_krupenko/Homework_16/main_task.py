import dotenv
import pymysql as mysql
import os
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(mysql.cursors.DictCursor)

all_data = '''
SELECT s.name, s.second_name, g.title as group_title, b.title as book_title,
       sub.title as subject_title, l.title as lesson_title, m.value as mark_value
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects sub ON l.subject_id = sub.id
'''

cursor.execute(all_data)
data_db = cursor.fetchall()
db.close()

base_path = os.path.dirname(__file__)

file_path = os.path.join(
    os.path.dirname(os.path.dirname(base_path)
                    ), "eugene_okulik", "Lesson_16", "hw_data", "data.csv"
)


data = []
with open(file_path, 'r', encoding='utf-8') as file:
    read = csv.DictReader(file)
    for row in read:
        data.append(row)

missed_data = []
for i in data:
    if i not in data_db:
        missed_data.append(i)

# print(missed_data)
for row in missed_data:
    print(f" name: {row['name']}, second_name: {row['second_name']}, group_title: {row['group_title']},"
          f" group_title: {row['book_title']}, subject_title: {row['subject_title']},"
          f" lesson_title: {row['lesson_title']}, mark_value: {row['mark_value']}")
