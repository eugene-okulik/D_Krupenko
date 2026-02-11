result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'


def task_3(result):
    result_index1 = result.index(": ") + 2
    a = int(result[result_index1:])
    print(a + 10)


task_3(result1)
task_3(result2)
task_3(result3)
