from datetime import datetime

origin_date_format = "Jan 15, 2023 - 12:05:33"

date_format_for_python = datetime.strptime(origin_date_format, "%b %d, %Y - %H:%M:%S")

month_full_name = date_format_for_python.strftime("%B")
print(month_full_name)

expected_date_format = date_format_for_python.strftime("%d.%m.%Y, %H:%M")
print(expected_date_format)

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25,
                29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_days = list(filter(lambda t: t > 28, temperatures))
print(hot_days)

max_temp = max(hot_days)
min_temp = min(hot_days)
avg_temp = sum(hot_days) / len(hot_days)

print(max_temp)
print(min_temp)
print(round(avg_temp, 1))