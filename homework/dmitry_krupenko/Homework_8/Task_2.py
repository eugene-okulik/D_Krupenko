def fibonacci(limit=10001):
    a, b = 0, 1
    count = 1
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


gen = fibonacci(10001)

# n5 = n200 = n1000 = n10000 = None - возможно, надо было создать эти переменные с пустыми значениями
# для большей наглядности
for i, value in enumerate(gen, start=1):
    if i == 5:
        n5 = value
    elif i == 200:
        n200 = value
    elif i == 1000:
        n1000 = value
    elif i == 10000:
        n10000 = value
        break

print(f"5-е: {n5}\n200-е: {n200}\n1000-е: {n1000}\n10000-е: {n10000}")
