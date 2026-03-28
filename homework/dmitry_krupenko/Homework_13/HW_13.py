import os
import datetime

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
target_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
# print(eugene_path)

with open(target_file_path, encoding='utf-8') as target_file:
    for line in target_file:
        before_dash = line.split(' - ')[0]
        date_string = before_dash.split(' ', 1)[1]
        date = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')

        if line.startswith("1."):
            print(date + datetime.timedelta(days=7))

        elif line.startswith("2."):
            print(date.strftime('%A'))

        elif line.startswith("3."):
            print((datetime.datetime.now() - date).days)
